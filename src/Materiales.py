class Materiales:
    #constructor
    def __init__(self, tb_index, cat_fila, cat_disciplina, cat_item_code, cat_size, cat_matl_type, cat_item_type, cat_descripcion, req_log, req_numero, req_descripcion_suplemento, req_numero_1, req_status, req_cantidad, req_total, req_uom, noc, noc_linea, noc_sub_linea, noc_destino, noc_cantidad, noc_fecha_ras, noc_fecha_sop, noc_grupo_de_embarque, noc_cantidad_grupo_de_embarque, noc_hito, noc_estatus, noc_fecha, noc_sh_hito, noc_sh_estatus, noc_sh_fecha
    ):
        self.__tb_index = tb_index
        self.__cat_fila = cat_fila
        self.__cat_disciplina = cat_disciplina
        self.__cat_item_code = cat_item_code
        self.__cat_size = cat_size
        self.__cat_matl_type = cat_matl_type
        self.__cat_item_type = cat_item_type
        self.__cat_descripcion = cat_descripcion
        self.__req_log = req_log
        self.__req_numero = req_numero
        self.__req_descripcion_suplemento = req_descripcion_suplemento
        self.__req_numero_1 = req_numero_1
        self.__req_status = req_status
        self.__req_cantidad = req_cantidad
        self.__req_total = req_total
        self.__req_uom = req_uom
        self.__noc = noc
        self.__noc_linea = noc_linea
        self.__noc_sub_linea = noc_sub_linea
        self.__noc_destino = noc_destino
        self.__noc_cantidad = noc_cantidad
        self.__noc_fecha_ras = noc_fecha_ras
        self.__noc_fecha_sop = noc_fecha_sop
        self.__noc_grupo_de_embarque = noc_grupo_de_embarque
        self.__noc_cantidad_grupo_de_embarque = noc_cantidad_grupo_de_embarque
        self.__noc_hito = noc_hito
        self.__noc_estatus = noc_estatus
        self.__noc_fecha = noc_fecha
        self.__noc_sh_hito = noc_sh_hito
        self.__noc_sh_estatus = noc_sh_estatus
        self.__noc_sh_fecha=noc_sh_fecha

    #retornar Materiales
    def info(self):
        return self.__tb_index,self.__cat_fila,self.__cat_disciplina,self.__cat_item_code,self.__cat_size,self.__cat_matl_type,self.__cat_item_type,self.__cat_descripcion,self.__req_log,self.__req_numero,self.__req_descripcion_suplemento,self.__req_numero_1,self.__req_status,self.__req_cantidad,self.__req_total,self.__req_uom,self.__noc,self.__noc_linea,self.__noc_sub_linea,self.__noc_destino,self.__noc_cantidad,self.__noc_fecha_ras,self.__noc_fecha_sop,self.__noc_grupo_de_embarque,self.__noc_cantidad_grupo_de_embarque,self.__noc_hito,self.__noc_estatus,self.__noc_fecha,self.__noc_sh_hito,self.__noc_sh_estatus,self.__noc_sh_fecha
        


""" 
materiales=Materiales(1,	1,	1,	"1250003021",	"<No Size>",	"B",	"MATERIALES",	"PA 1-1/2 L=1300 mm ASTMF1554 grado 36 +  2 tuercas hex ASTMA563Gr A +  Golilla ASTMF436 + 1 tuerca hex ASTMA563GrA",	"1-01020",	"1-01020-FLD-RQ",	"PERNOS DE ANCLAJE Y ROCA DE TUNELES",	1,	"P",	610,	2625,	"EA",	"B1PA-1-01020-01",	1,	0,	"FLD",	2015,	"01-Feb-24",	"02-Oct-24", "","","","","","","","")
print(materiales.info())

 """