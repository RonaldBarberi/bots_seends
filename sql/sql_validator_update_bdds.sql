SELECT
	campana,
    'tb_bdd_claro_hogar_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_claro_hogar_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_operacion_hogar_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_operacion_hogar_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_novus_hogar_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_novus_hogar_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_claro_migracion_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_claro_migracion_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_operacion_migracion_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_operacion_migracion_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_novus_migracion_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_novus_migracion_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_claro_portabilidad_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_claro_portabilidad_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_operacion_portabilidad_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_operacion_portabilidad_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59')
UNION ALL
SELECT
	campana,
    'tb_bdd_novus_portabilidad_dts' `table`,
    MAX(date_last_trx) date_last_trx,
    MAX(date_last_sms) date_last_sms,
    MAX(date_last_ivr) date_last_ivr,
    MAX(date_last_inb) date_last_inb,
    MAX(date_last_out) date_last_out,
    MAX(date_last_blaster) date_last_blaster,
    MAX(date_last_whastapp) date_last_whastapp
FROM bbdd_cs_bog_tmk.tb_bdd_novus_portabilidad_dts
WHERE date_last_trx BETWEEN DATE_FORMAT(SUBDATE(CURDATE(), 3), '%%Y-%%m-%%d 00:00:00') AND DATE_FORMAT(CURDATE(), '%%Y-%%m-%%d 23:59:59');