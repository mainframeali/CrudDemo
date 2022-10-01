# define base request objects for listing
from pydantic import BaseModel, Field


class ListingRequest(BaseModel):
    address: str = Field(
        None, title="Property Name", max_length=1000
    )
    price: float = Field(..., gt=0,
                         description="Listing Price")


class ListingUpdateRequest(BaseModel):
    listing_id: int
    address: str = Field(
        None, title="Property Address", max_length=1000
    )
    price: float = Field(..., gt=0,
                         description="The price must be greater than zero")

