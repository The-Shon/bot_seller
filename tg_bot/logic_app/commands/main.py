from .h_user_start import user_router_start
from .h_user_catalog import user_router_catalog
from .h_user_make_order import user_router_make_order
from .h_user_track_order import user_router_track_order
from .h_user_other import user_router_other
from .h_user_comm_info import user_router_comm_info

routers = (user_router_start, 
           user_router_catalog, 
           user_router_make_order, 
           user_router_track_order,
           user_router_comm_info,
           user_router_other)