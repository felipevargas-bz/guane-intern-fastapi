from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from schemas.user import (
    CreateUser,
    SearchUser,
    UpdateUser,
    User
    )
from services.user import user_service

router = APIRouter()


@router.get(
    path="/api/users",
    tags=["User"],
    summary="Get All Users"
)
async def get_users():
    """
    Get All Users

    In this path operation, a query is made to the database
    to obtain all the registered users, then the information
    is stored in a list.

    Parameters:

        ...

    Return:

        Returns a list of users registered in the database.

    """
    pass


@router.get(
    path="/api/users/{user_email}",
    tags=["User"],
    summary="Get User By Email"
)
async def get_user():
    """
    Get User By Email

    In this path operation, a query is made to the database
    to obtain the information of a user through their Email.

    Parameters:

        - user_email: String

    Return:

        Returns an users registered in the database.

    """
    pass


@router.get(
    path="/api/users/dogs/{user_email}",
    tags=["User"],
    summary="Get All The Dogs Of An User By Email"
)
async def user_dogs():
    """
    Get All The Dogs Of An User

    In this route operation, a query is made to the database
    through the user's email to obtain all the registered dogs
    associated with this user, then the information is stored in a list.

    Parameters:

        - user_email: String

    Return:

        Returns a list with the information of all the dogs registered
        in the database that are associated with a certain user

    """
    pass


@router.post(
    path="/api/users",
    response_model=User,
    tags=["User"],
    summary="Register An User"
)
async def create_user(new_user: CreateUser):
    """
    Register An User

    In this path operation a user is registered in the database.

    Parameters:

        - id: Integer
        - first_name: String
        - last_name: String
        - email: String
        - create_date: datetime
        - update_date: datetime

    Return:

        Returns a confirmation message that the user has been registered
        in the database.
    """
    user = await user_service.get_by_email(email=new_user.email)
    if user is not None:
        raise HTTPException(status_code=400, detail="user already exists in database")
    user = await user_service.create(obj_in=new_user)

    return user


@router.put(
    path="/api/users/{user_email}",
    tags=["User"],
    summary="Update An User By Email"
)
async def update_user():
    """
    Update An User

    In this path operation we make a query to the database through the id
    of a user to obtain his information, then with the data sent by the
    client we respectively replace each attribute.

    Parameters:

        - id: Integer
        - first_name: String
        - last_name: String
        - email: String
        - create_date: datetime
        - update_date: datetime

    Return:

        Returns a confirmation message that the user has been updated
        in the database.
    """
    pass


@router.delete(
    path="/api/users/{user_email}",
    tags=["User"],
    summary="Delete An User By Email"
)
async def delete_user():
    """
    Update An User

    In this path operation, a query is made to the database through the
    email of a user for the elimination of this.

    Parameters:

        - user_email: String

    Return:

        Returns a confirmation message that the user has been deleted
        from database.
    """
    pass
