# Python


# FastApi
from typing import List
from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException, Path, Query

# Local
from schemas.dog import (
    CreateDog,
    SearchDog,
    UpdateDog,
    Dog
    )
from services.dog import dog_service
from services.user import user_service


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
    return await dog_service.get_all()


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
    all_dogs = await dog_service.get_all()

    return [dog for dog in all_dogs if dog.__dict__["is_adopted"] == True]

@router.get(
    path="/api/dogs/{dog_id}",
    tags=["Dog"],
    summary="Get Dog By ID"
)
async def dog_id(dog_id: int):
    """
    Get a Dog

    This path operation makes a query to the database
    obtaining the information of a dog through its ID

    Parameters:

        - dog_id: int

    Return:

        Returns the information of a dog registered in the database
    """
    return await dog_service.get_by_id(dog_id)

@router.post(
    path="/api/dogs",
    response_model=Dog,
    tags=["Dog"],
    summary="Register a Dog"
)
async def create_dog(new_dog: CreateDog):
    """
    Register a Dog

    In this path operation, a dog is created and then stored
    in the database. For the picture field, an external API
    is consumed from where the url of a random image is obtained.

    Parameters:

        - id: Integer
        - name: String
        - picture: String
        - is_adopted: Boolean
        - create_date: Datetime
        - update_date: Datetime
        - id_user: Integer

    Return:

        Returns a confirmation message of the dog's registration
        in the database
    """
    dog = await dog_service.create(obj_in=new_dog)
    return dog

@router.put(
    path="/api/dogs/{dog_id}",
    tags=["Dog"],
    summary="Update a dog by ID"
)
async def update_dog():
    """
    Update a Registered Dog

    In this path operation, a query is made to the database
    through the ID to obtain a registered dog, after obtaining
    this information, we take the data that was sent from the
    client, replacing respectively as specified in the parameters.

    Parameters:

        - id: Integer
        - name: String
        - picture: String
        - is_adopted: Boolean
        - create_date: Datetime
        - update_date: Datetime
        - id_user: Integer

    Return:

        Returns a confirmation message of the dog update in the database.
    """
    pass

@router.delete(
    path="/api/dogs/{dog_id}",
    tags=["Dog"]
)
async def delete_dog(dog_id: int):
    """
    Delete Dog

    In this path operation, a dog is created and then stored
    in the database. For the picture field, an external API
    is consumed from where the url of a random image is obtained.

    Parameters:

        - id: Integer
        - name: String
        - picture: String
        - is_adopted: Boolean
        - create_date: Datetime
        - update_date: Datetime
        - id_user: Integer

    Return:

        Returns a confirmation message of the dog's registration
        in the database
    """
    pass
