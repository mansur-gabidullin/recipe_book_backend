from typing import runtime_checkable, Protocol
from uuid import UUID

from .new_product_response_model import INewProductResponseModel
from .product_response_model import IProductResponseModel


@runtime_checkable
class IProductResponseConverter(Protocol):
    def from_products(self, products) -> list[IProductResponseModel]:
        ...

    def from_new_product(self, uuid: UUID) -> INewProductResponseModel:
        ...
