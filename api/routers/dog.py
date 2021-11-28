"""
define the routes of our api,
working with the scheme below.
    ___________Dog___________
    |+ id: integer          |
    |+ name: String         |
    |+ picture: String      |
    |+ is_adopted: Boolean  |
    |+ create_date: Datetime|
"""
# Python


# FastApi
from fastapi import APIRouter


router = APIRouter()


@router.get(
    path="/api/dogs",
    tags=["Dog"],
    summary="Get All Dogs"
)
async def dogs():
    """
    Get All Dogs

    This path operation makes a query to the database
    obtaining all registered dogs and stores them in a
    list to be returned later.

    Parameters:

        ...

    Return:

        Our dogs list, FastApi automatically converts
        it to JSON, returning a JSON with the data from the
        List containing all registered dogs.
    """
    pass


@router.get(
    path="/api/dogs/is_adopted",
    tags=["Dog"],
    summary="Get All Adopted Dogs"
)
async def is_adopted():
    """
    Dogs is Adopted

    This path operation performs a query to the database,
    obtaining all registered dogs where its is_adopted
    attribute is true, Then it stores those dogs in a
    list to later be returned..

    Parameters:

        ...

    Return:

        Our dictionary list, FastApi automatically converts
        it to JSON, returning a JSON with the data from the
        List containing all registered dogs.

    """
    pass

@router.get(
    path="/api/dogs/{dog_id}",
    tags=["Dog"],
    summary="Get Dog By ID"
)
async def dog_id():
    """
    Get a Dog

    This path operation makes a query to the database
    obtaining the information of a dog through its ID

    Parameters:

        - dog_id: int

    Return:

        Returns the information of a dog registered in the database
    """
    pass

@router.post(
    path="/api/dogs",
    tags=["Dog"],
    summary="Register a Dog"
)
async def create_dog():
    """
    Register a Dog

    In this path operation, a dog is created and then stored
    in the database. For the picture field, an external API
    is consumed from where the url of a random image is obtained.

    Parameters:

        - id: int
        - name: str
        - picture: str
        - is_adopted: Bool
        - create_date: datetime

    Return:

        Returns a confirmation message of the dog's registration
        in the database
    """
    pass

@router.put(
    path="/api/dogs/{dog_id}",
    tags=["Dog"],
    summary=""
)
async def update_dog():
    """Update a record (dog) by name"""
    pass

@router.delete("/api/dogs/{name}", tags=["Dog"])
async def delete_dog():
    """Delete a record (dog) by name."""
    pass
