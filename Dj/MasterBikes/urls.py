from django.urls import path
from MasterBikes import views

urlpatterns = [

    path('login', views.conectar, name='login'),
    path('logout', views.desconectar, name='logout'),
    path('registrar', views.registrar, name='registrar'),

    path('', views.Principal, name='Principal'),
    path('arriendo', views.arriendo, name='arriendo'),
    path('mantencion',views.Mantencion, name='mantencion'),
    path('nosotros',views.Nosotros, name='nosotros'),
    path('registro',views.Registro, name='registro'),
    path('tienda',views.Tienda, name='tienda'),
    path('tienda-indumentaria',views.Tienda_indumentaria, name='tienda-indumentaria'),
    path('ver-producto/<int:id_prod>',views.VerProducto, name='ver-producto'),

    path('pago-carrito',views.pago_carrito, name='pago-carrito'),
    path('addToCart',views.addToCart, name='addToCart'),
    path('pagarCart',views.pagarCart, name='pagarCart'),
    path('delToCart/<str:pk>',views.delToCart, name='delToCart'),

    path('crud-varios', views.crud_varios, name='crud-varios'),
    path('crud-usuarios', views.crud_usuarios, name='crud-usuarios'),
    path('crud-arriendos', views.crud_arriendos, name='crud-arriendos'),
    path('crud-productos', views.crud_productos, name='crud-productos'),
    path('crud-reparaciones', views.crud_reparacion, name='crud-reparaciones'),
    path('crud-ventas/<int:pk>', views.crud_ventas, name='crud-ventas'),
    path('crud-despacho/<int:pk>', views.crud_despacho, name='crud-despacho'),
    path('add-tipo-usuario', views.add_tipoUsuario, name='add-tipo-usuario'),
    path('add-usuario', views.add_usuario, name='add-usuario'),
    path('del-usuario/<str:pk>', views.del_usuario, name='del-usuario'),
    path('edit-usuario/<str:pk>', views.edit_usuario, name='edit-usuario'),
    path('edit-tipo-usuario/<str:pk>', views.edit_tipoUser, name='edit-tipo-usuario'),
    path('del-tipo-usuario/<str:pk>', views.del_tipoUser, name='del-tipo-usuario'),
    path('add-talla', views.add_talla, name='add-talla'),
    path('del-talla/<str:pk>', views.del_talla, name='del-talla'),
    path('add-bici', views.add_bici, name='add-bici'),
    path('add-forma-pago', views.add_forma_pago, name='add-forma-pago'),
    path('add-tipo-producto', views.add_tipo_producto, name='add-tipo-producto'),
    path('add-estado', views.add_estado, name='add-estado'),
]

""" path('edit-tipo-usuario', views.edit_tipoUsuario, name='edit-tipo-usuario'), """