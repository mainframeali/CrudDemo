# define get, insert, update & delete methods
from fastapi import APIRouter
from model.request import ListingRequest, ListingUpdateRequest
from model.response import response
from model.listing import Listing
from db.database import Database
from sqlalchemy import and_, desc

# APIRouter creates path operations for product module
router = APIRouter(
    prefix="/listings",
    tags=["Listing"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post("/add", response_description="Listing data added into the database")
async def add_listing(listing_req: ListingRequest):
    # prepare listing object
    new_listing = Listing()
    new_listing.address = listing_req.address
    new_listing.price = listing_req.price
    session = database.get_db_session(engine)
    session.add(new_listing)
    session.flush()
    # get id of the inserted product
    session.refresh(new_listing, attribute_names=['listing_id'])
    data = {"listing_id": new_listing.listing_id}
    session.commit()
    session.close()
    return response(data, 200, "Listing added successfully.", False)


@router.put("/update")
async def update_listing(listing_update_req: ListingUpdateRequest):
    listing_id = listing_update_req.listing_id
    session = database.get_db_session(engine)
    try:
        is_listing_updated = session.query(Listing).filter(Listing.listing_id == listing_id).update({
            Listing.address: listing_update_req.address, Listing.price: listing_update_req.price
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Listing updated successfully"
        response_code = 200
        error = False
        if is_listing_updated == 1:
            # After successful update, retrieve updated data from db
            data = session.query(Listing).filter(
                Listing.listing_id == listing_id).one()
        elif is_listing_updated == 0:
            response_msg = "Listing not updated. No Listing found with this id :" + \
                str(listing_id)
            error = True
            data = None
        return response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.delete("/{listing_id}/delete")
async def delete_listing(listing_id: int):
    session = database.get_db_session(engine)
    try:
        is_deleted = session.query(Listing).filter(Listing.listing_id == listing_id).delete()
        session.flush()
        session.commit()
        response_msg = "Listing deleted successfully"
        response_code = 200
        error = False
        data = {"listing_id": listing_id}
        if is_deleted == 0:
            response_msg = "Listing not deleted. No Listing found with this id :" + \
                str(listing_id)
            error = True
            data = None
        return response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.get("/{listing_id}")
async def read_product(listing_id: int):
    session = database.get_db_session(engine)
    response_message = "Listing retrieved successfully"
    data = None
    try:
        data = session.query(Listing).filter(Listing.listing_id == listing_id).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Listing Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_listings(page_size: int, page: int):
    session = database.get_db_session(engine)
    data = session.query(Listing).order_by(
        desc(Listing.listing_id)).limit(page_size).offset((page-1)*page_size).all()
    return response(data, 200, "Products retrieved successfully.", False)

