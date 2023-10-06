from datetime import timedelta
from typing import List, Optional
from fastapi import APIRouter, status, Request, Response, Body
from app.models import order as orderModel
from app.services import service_order
from fastapi_redis_cache import cache

router = APIRouter()

@router.post("/solution")
@cache(expire=timedelta(minutes=3))
async def process_orders(request: Request, orderRequest: orderModel.OrderRequest = Body(...)):
    total_price = service_order.process_orders(orderRequest.orders, orderRequest.criterion)
    print(f"Ingresos totales para órdenes '{orderRequest.criterion}' es: ${total_price}")
    return  total_price


