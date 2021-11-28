from fastapi import APIRouter



router = APIRouter()


@router.get(
    path="/api/users",
    tags=["User"],
    summary="Get All Users"
)
async def get_users():
    """Get a list of all users"""
    pass


@router.get(
    path="/api/users/{user_email}",
    tags=["User"],
    summary="Get User By Email"
)
async def get_user():
    """get user by email"""
    pass


@router.get(
    path="/api/users/dogs/{user_email}",
    tags=["User"],
    summary="Get All The Dogs Of An User By Email"
)
async def user_dogs():
    """Get all the dogs of an user"""
    pass


@router.post(
    path="/api/users",
    tags=["User"],
    summary="Register An User"
)
async def create_user():
    """create an user by email"""
    pass


@router.put(
    path="/api/users/{user_email}",
    tags=["User"],
    summary="Update An User By Email"
)
async def update_user():
    """update an user"""
    pass


@router.delete(
    path="/api/users/{user_email}",
    tags=["User"],
    summary="Delete An User By Email"
)
async def delete_user():
    """delete user by email"""
    pass
