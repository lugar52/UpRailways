class Equipos:
    #Constructor
    def __init__(self, cat_fila,cat_disciplina,cat_matl_type,cat_tag_number,cat_descripcion,cat_cwp,cat_cwp_descripcion,cat_contrato,cat_destino,cat_estado,req_log,req_req_numero,req_descripcion_suplemento,req_numero,req_status,req_cantidad,req_total,sol_rfq_numero,sol_hito,sol_estatus,sol_fecha,sol_sig_hito,sol_sig_hito_estatus,sol_sig_hito_fecha,orc_numero_oc,orc_linea,orc_sub_linea,orc_destino,orc_cantidad,orc_fecha_ras,orc_fecha_sop,orc_grupo_de_embarque,orc_hito,orc_estatus,orc_fecha,orc_sig_hito,orc_sig_hito_estatus,orc_sig_hito_fecha,tb_index):
        self.__cat_fila=cat_fila
        self.__cat_disciplina=cat_disciplina
        self.__cat_matl_type=cat_matl_type
        self.__cat_tag_number=cat_tag_number
        self.__cat_descripcion=cat_descripcion
        self.__cat_cwp=cat_cwp
        self.__cat_cwp_descripcion=cat_cwp_descripcion
        self.__cat_contrato=cat_contrato
        self.__cat_destino=cat_destino
        self.__cat_estado=cat_estado
        self.__req_log=req_log
        self.__req_req_numero=req_req_numero
        self.__req_descripcion_suplemento=req_descripcion_suplemento
        self.__req_numero=req_numero
        self.__req_status=req_status
        self.__req_cantidad=req_cantidad
        self.__req_total=req_total
        self.__sol_rfq_numero=sol_rfq_numero
        self.__sol_hito=sol_hito
        self.__sol_estatus=sol_estatus
        self.__sol_fecha=sol_fecha
        self.__sol_sig_hito=sol_sig_hito
        self.__sol_sig_hito_estatus=sol_sig_hito_estatus
        self.__sol_sig_hito_fecha=sol_sig_hito_fecha
        self.__orc_numero_oc=orc_numero_oc
        self.__orc_linea=orc_linea
        self.__orc_sub_linea=orc_sub_linea
        self.__orc_destino=orc_destino
        self.__orc_cantidad=orc_cantidad
        self.__orc_fecha_ras=orc_fecha_ras
        self.__orc_fecha_sop=orc_fecha_sop
        self.__orc_grupo_de_embarque=orc_grupo_de_embarque
        self.__orc_hito=orc_hito
        self.__orc_estatus=orc_estatus
        self.__orc_fecha=orc_fecha
        self.__orc_sig_hito=orc_sig_hito
        self.__orc_sig_hito_estatus=orc_sig_hito_estatus
        self.__orc_sig_hito_fecha=orc_sig_hito_fecha
        self.__tb_index=tb_index

    #Retornar Equipos
    def info(self):
        return self.__cat_fila,self.__cat_disciplina,self.__cat_matl_type,self.__cat_tag_number,self.__cat_descripcion,self.__cat_cwp,self.__cat_cwp_descripcion,self.__cat_contrato,self.__cat_destino,self.__cat_estado,self.__req_log,self.__req_req_numero,self.__req_descripcion_suplemento,self.__req_numero,self.__req_status,self.__req_cantidad,self.__req_total,self.__sol_rfq_numero,self.__sol_hito,self.__sol_estatus,self.__sol_fecha,self.__sol_sig_hito,self.__sol_sig_hito_estatus,self.__sol_sig_hito_fecha,self.__orc_numero_oc,self.__orc_linea,self.__orc_sub_linea,self.__orc_destino,self.__orc_cantidad,self.__orc_fecha_ras,self.__orc_fecha_sop,self.__orc_grupo_de_embarque,self.__orc_hito,self.__orc_estatus,self.__orc_fecha,self.__orc_sig_hito,self.__orc_sig_hito_estatus,self.__orc_sig_hito_fecha,self.__tb_index,
