from typing import TypeVar, Generic, List, Dict, Any, Optional
from fastapi import Query, Request
from pydantic import BaseModel
from sqlalchemy.orm import Query as SQLAlchemyQuery
from math import ceil
from app.schemas.web_response import Paging

T = TypeVar("T")

class PageParams:
    def __init__(
        self, 
        page: Optional[int] = Query(1, ge=1, description="Page number, starting from 1"),
        size: Optional[int] = Query(10, ge=1, le=100, description="Number of items per page")
    ):
        self.page = page or 1
        self.size = size or 10
        self.offset = (self.page - 1) * self.size

class PaginationEngine:
    """
    A reusable pagination engine for SQLAlchemy queries.
    
    Example usage in a repository:
    ```
    def get_projects_paginated(self, page_params: PageParams):
        query = self.db.query(Project)
        paginated_result = PaginationEngine.paginate(query, page_params)
        return paginated_result
    ```
    """
    @staticmethod
    def paginate(query: SQLAlchemyQuery, page_params: PageParams) -> Dict[str, Any]:
        """
        Paginate a SQLAlchemy query according to the provided pagination parameters.
        
        Returns a dictionary with the following keys:
        - items: The paginated items
        - paging: A dict with pagination metadata
        """
        # Get the total count before applying pagination
        total_count = query.count()
        
        # Apply pagination to the query
        items = query.offset(page_params.offset).limit(page_params.size).all()
        
        # Calculate total pages
        total_pages = ceil(total_count / page_params.size) if total_count > 0 else 0
        
        # Prepare paging metadata as a dictionary
        paging = {
            "page": page_params.page,
            "size": page_params.size,
            "totalItems": total_count,
            "totalPages": total_pages
        }
        
        return {
            "items": items,
            "paging": paging
        }
