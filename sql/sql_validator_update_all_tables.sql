SELECT 'tb_marcaciones_desgloce_dts' `table`, MAX(call_date) last_update
FROM bbdd_cs_bog_tmk.tb_marcaciones_desgloce_dts
WHERE call_date BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_bdd_ventas_tmk_dts' `table`, MAX(fecha_venta) last_update
FROM bbdd_cs_bog_tmk.tb_bdd_ventas_tmk_dts
WHERE fecha_venta BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 7), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_desglose_soul_dts' `table`, MAX(fecha_creacion) last_update
FROM bbdd_cs_bog_tmk.tb_desglose_soul_dts
WHERE fecha_creacion BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_bdd_ventas_tmk_soul_dts' `table`, MAX(fecha_venta) last_update
FROM bbdd_cs_bog_tmk.tb_bdd_ventas_tmk_soul_dts
WHERE fecha_venta BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_blacklist' `table`, MAX(upload_date) last_update
FROM bbdd_cs_bog_tmk.tb_blacklist
UNION ALL
SELECT 'tb_infobip_sms' `table`, MAX(`Send At`) last_update
FROM bbdd_cs_bog_tmk.tb_infobip_sms
WHERE `Send At` BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_infobip_sms_diario_cliente' `table`, MAX(date_last_sms) last_update
FROM bbdd_cs_bog_tmk.tb_infobip_sms_diario_cliente
WHERE date_last_sms BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_infobip_sms_mensual_cliente' `table`, MAX(date_last_sms) last_update
FROM bbdd_cs_bog_tmk.tb_infobip_sms_mensual_cliente
WHERE date_last_sms BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_kronos_sms' `table`, MAX(enviado) last_update
FROM bbdd_cs_bog_tmk.tb_kronos_sms
WHERE enviado BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_kronos_sms_diario_cliente' `table`, MAX(date_last_sms) last_update
FROM bbdd_cs_bog_tmk.tb_kronos_sms_diario_cliente
WHERE date_last_sms BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_kronos_sms_mensual_cliente' `table`, MAX(date_last_sms) last_update
FROM bbdd_cs_bog_tmk.tb_kronos_sms_mensual_cliente
WHERE date_last_sms BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_infobip_voice_and_video' `table`, MAX(`Send At`) last_update
FROM bbdd_cs_bog_tmk.tb_infobip_voice_and_video
WHERE `Send At` BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_infobip_ivr_diario_cliente' `table`, MAX(date_last_ivr) last_update
FROM bbdd_cs_bog_tmk.tb_infobip_ivr_diario_cliente
WHERE date_last_ivr BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_infobip_ivr_mensual_cliente' `table`, MAX(date_last_ivr) last_update
FROM bbdd_cs_bog_tmk.tb_infobip_ivr_mensual_cliente
WHERE date_last_ivr BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_intico_sms' `table`, MAX(`Fecha Envio`) last_update
FROM bbdd_cs_bog_tmk.tb_intico_sms
WHERE `Fecha Envio` BETWEEN SUBDATE(CURDATE(), 3) AND CURDATE()
UNION ALL
SELECT 'tb_intico_sms_diario_cliente' `table`, MAX(date_last_sms) last_update
FROM bbdd_cs_bog_tmk.tb_intico_sms_diario_cliente
WHERE date_last_sms BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_intico_sms_mensual_cliente' `table`, MAX(date_last_sms) last_update
FROM bbdd_cs_bog_tmk.tb_intico_sms_mensual_cliente
WHERE date_last_sms BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_kronos_ivr' `table`, MAX(`Fecha evento`) last_update
FROM bbdd_cs_bog_tmk.tb_kronos_ivr
WHERE `Fecha evento` BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT 'tb_messages_what_claroventas_rpa' `table`, MAX(MES_CREATION_DATE) last_update
FROM bbdd_cs_bog_tmk.tb_messages_what_claroventas_rpa
WHERE MES_CREATION_DATE BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59');
