import os
import requests

# Lista de URLs de las imágenes
image_urls = [
    {'name':'TEQUILA_CORRALEJO_REPOSADO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/CORRALEJO-REPOSADO.jpg'},
    {'name':'VINO_ARG_ZUCCARDI_MALAMADO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Malamado.jpg'},
    {'name':'VINO_CH_MONTES_ALPHA_CAB_SAUV.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Alpha-Cabernet-Sauvignon.jpg'},
    {'name':'VINO_CH_DONA_DOMINGA_CARMENERE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/07/DONA-DOMINGA-CARMENERE.jpg'},
    {'name':'VINO_ARG_ALTA_VISTA_TORRONTES_CLASSIC.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/ALTA-VISTA-TORRONTES-CLASSIC1.png'},
    {'name':'VAPE_VOZOL_STAR_3000_COTTON_CANDY_ICE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-3000-COTTON-CANDY-ICE.png'},
    {'name':'VINO_ARG_TRAPICHE_MEDALLA_CAB_SAUV.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Medalla-Cabernet-Sauvignon.jpg'},
    {'name':'VINO_ARG_LUCA_MALBEC.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/LUCA-MALBEC.jpg'},
    {'name':'VINO_TINTO_CABERNET_MERLOT_RUTINI.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Reserva-Chardonnay.jpg'},
    {'name':'FUNDA_DE_HIELO_180kg.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/hielo-180kg.png'},
    {'name':'VINO_ARG_DONA_PAULA_ESTATE_MALBEC.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Estate-Malbec.jpg'},
    {'name':'LINDT_MINI_PRALINES_100g.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/lindt-mini-pralines.png'},
    {'name':'VINO_AUST_PENFOLDS_KH_SHIRAZCABERNET.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2022/06/PENFOLDS-KH-SHIRAZ.CAB_.png'},
    {'name':'VINO_AUST_PENFOLDS_KH_SHIRAZCABERNET.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/CHOCOLATE-KAMM-SALTY-CARAMEL-60g.png'},
    {'name':'VAPE_VOZOL_STAR_3000_FORREST_BERRY_STORM.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-3000-FOREST-BERRY-STORM.png'},
    {'name':'VINO_CH_CASA_SILVA_SAUV_BLANC_RESV.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/02/CASA-SILVA-SAUV.-BLANC.jpg'},
    {'name':'VINO_ARG_SANTA_JULIA_CHARDONNAY.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Chardonnay.jpg'},
    {'name':'CHOCOLATE_KAMM_BIG_MANGO_60g.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/CHOCOLATE-KAMM-BIG-MANGO-60g.png'},
    {'name':'SIXPACK_CERVEZA_CLUB_PLATINO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/06/SIXPACK-CERVEZA-CLUB-PALTINO-LATA-355ML.png'},
    {'name':'VINO_ARG_LUCA_NICO_BY_LUCA_MALBEC.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Nico.jpg'},
    {'name':'CREMA_MAZERATTO_WHISKY_Y_VAINILLA_BOTELLA_DOBLE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/CREMA-MAZERATTO-WHISKY-Y-VAINILLA-BOTELLA-DOBLE-750ml.png'},
    {'name':'PROMO_MUCHO_MAS_X_2_EN_1999.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2022/09/MUCHO-MAS-2.png'},
    {'name':'PACK_RON_SAN_MIGUEL_PLATA_+_VASOS.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/02/RON-SAN-MIGUEL-BLANCO-VASO.png'},
    {'name':'VINO_ARG_EL_GRAN_ENEMIGO_SV_GUALTALLARY.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2020/09/GRAN-ENEMIGO-GUALTALLARY-1.jpg'},
    {'name':'VINO_CH_MONTES_ALPHA_SYRAH.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Alpha-Syrah.jpg'},
    {'name':'BRANDY_DE_JEREZ_SOLERA_GRAN_RESERVA_LEPANTO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/BRANDY-LEPANTO-GRAN-RESERVA-SOLERA.jpg'},
    {'name':'VINO_CH_MONTES_ALPHA_CARMENERE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/MONTES-ALPHA-CARMENERE.jpg'},
    {'name':'VINO_ARG_FIN_DEL_MUNDO_CAB_SAUVMALBEC.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/10/FIN-DEL-MUNDO-CAB.-SAUV-MALBEC.jpg'},
    {'name':'VINO_AMELIA_CHARDONNAY.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Amelia-Chardonnay.jpg'},
    {'name':'GIN_HALF_CROWN.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2019/08/HALF-CROWN-GIN.jpg'},
    {'name':'VINO_CH_COUSINO_MACUL_GRIS.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Gris.jpg'},
    {'name':'CHOCOLATE_KAMM_GINGER_LEMONADE_60g.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/CHOCOLATE-KAMM-GINGER-LEMONADE-60g.png'},
    {'name':'PACK_VINO_RODA_+_RODA_SELA.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/01/PACK-RODA-RODA-SELA.png'},
    {'name':'FOSFORERA_BIC.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/FOSFORERA-BIC.png'},
    {'name':'VINO_ESP_RODA_I_CM_500ml_EN_TRIPACK.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2021/05/PACK-RODA-50.png'},
    {'name':'DUO_PACK_SOMETHING_SPECIAL_8_ANOS_+_SOMETHING_SPECIAL_8_ANOS.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2021/12/DUO-PACK-SOMETHING.png'},
    {'name':'4_PACK_AGUA_TONICA_CINCHONA_ORIGINAL_CON_AZUCAR.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/FOUR-PACK-CINCHONA-CON-AZUCAR.png'},
    {'name':'VAPE_VOZOL_STAR_4000_LUSH_ICE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-4000-LUSH-ICE.png'},
    {'name':'TEQUILA_CORRALEJO_BLANCO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/CORRALEJO-BLANCO.jpg'},
    {'name':'RITTER_CHOCOCUBO_YOGURT_MIX_176g.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/ritter-choco-cubes-yogurt-mix-176g1.png'},
    {'name':'VAPE_VOZOL_STAR_3000_TROPICAL_JUNGLE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-3000-JUNGLE-BIRD.png'},
    {'name':'VINO_ARG_ZUCCARDI_ALUVIONAL.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/02/ZUCCARDI-ALUVIONAL.jpg'},
    {'name':'COGNAC_REMY_MARTIN_VSOP.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2022/04/COGNAC-REMY-MARTIN-V.S.O.P.png'},
    {'name':'VINO_CH_MONTES_PINOT_NOIR_SELEC_LTDA.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/MONTES-PINOT-NOIR-SELEC.-LTDA.-750ML.jpeg'},
    {'name':'VAPE_VOZOL_STAR_3000_MANGO_PASSION_FRUIT.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-3000-MANGO-PASSION-FRUIT.png'},
    {'name':'GIN_MON_PEPINO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/GIN-MON-PEPINO-1000ml-2.png'},
    {'name':'VAPE_VOZOL_STAR_4000_KIWI_GUAVA_PASSION_FRUIT.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-4000-KIWI-GUAVA-PASSION-FRUIT.png'},
    {'name':'VINO_ESP_PENASOL_SANGRIA_TETRA_PACK.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/penasol-sangria.jpg'},
    {'name':'VINO_CH_MONTES_CAB_SAUVCARMENERE_SELEC_LTDA.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/MONTES-SELEC.-LTDA-CB-CARME.jpg'},
    {'name':'RITTER_CHOCOLATE_PRALINE_250g.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/ritte-chocolate-praline.png'},
    {'name':'PISCO_TABERNERO_PURO_ACHOLADO_700ML.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/TABERNERO-ACHOLADO-700.jpg'},
    {'name':'SIXPACK_CERVEZA_STELLA_ARTOIS.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2020/04/SIX-PACK-STELLA.jpg'},
    {'name':'CREMA_MAZERATTO_CAFE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/CREMA-MAZERATTO-CAFE.png'},
    {'name':'ENERGIZANTE_RED_BULL_SIN_AZUCAR.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/02/ENERGIZANTE-RED-BULL-SIN-AZUCAR-250ml.png'},
    {'name':'VAPE_VOZOL_STAR_4000_BLUEBERRY_STORM.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-4000-BLUEBERRY-STORM.png'},
    {'name':'RITTER_CHOCOLATE_CLECHE_ALPES_250g.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/ritter-chocolate-leche-alpes.png'},
    {'name':'VAPE_VOZOL_STAR_4000_COOL_MINT.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-4000-COOL-MINT.png'},
    {'name':'CREMA_MEETING_CURACAO_BLUE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/06/CREMA-MEETING-CURACAO-BLUE.png'},
    {'name':'SIXPACK_CERVEZA_CLUB_PLATINO_LATA.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/06/SIXPACK-CERVEZA-CLUB-PALTINO-LATA-355ML.png'},
    {'name':'PACK_RON_SAN_MIGUEL_ORO_+_VASOS.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/02/RON-SAN-MIGUEL-ORO-VASO.png'},
    {'name':'LINDOR_CORNET_SURTIDO_CHOCOLATE_CRELLENO_CREMOSO_200g.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/LINDOR-CORNET-SURTIDO-CHOCOLATE-LECHE-RELLENO-CREMOSO.png'},
    {'name':'VINO_CH_CHILCAS_RED_ONE_PREMIUM.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2021/03/RED-ONE.png'},
    {'name':'GB_QUESO_IBERICO_SEMICURADO_150gr.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2021/08/QUESO-IBERICO.png'},
    {'name':'TEQUILA_CORRALEJO_ANEJO_99000_HORAS.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2022/06/TEQUILA-CORRALEJO-99000.png'},
    {'name':'VINO_CH_MISIONES_DE_RENGO_CUVEE_CARMENERE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2020/05/MISIONES-DE-RENGO-CUVEE-GRAN-RESERVA-CARMENERE.png'},
    {'name':'GB_QUESO_DE_CABRA_150gr.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2021/08/QUESO-DE-CABRA.png'},
    {'name':'CHAMPAGNE_HENKELL_ROSE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/HENKELL-ROSE.png'},
    {'name':'COGNAC_HENNESSY_VSOP.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2022/04/COGNAC-HENNESSY-V.S.O.png'},
    {'name':'VINO_CH_DONA_DOMINGA_SAUV_BLANC_SEMILLON.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/07/DONA-DOMINGA-SAUV.-BLANC-SEMILLON.jpg'},
    {'name':'VAPE_VOZOL_STAR_4000_ALOE_GRAPE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-4000-ALOE-GRAPE.png'},
    {'name':'VINO_DE_JEREZ_XERES_SHERRY_FINO_MUY_SECO_PALOMINIO_FINO_TIO_PEPE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2017/12/Vino-de-Jerez-Palomino-Fino-Muy-Seco.jpg'},
    {'name':'VAPE_VOZOL_STAR_3000_BLUE_RAZZ_ICE.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/VAPE-VOZOL-3000-BLUE-RAZZ-ICE.png'},
    {'name':'GIN_CRUZ_LOMA.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/07/GIN-CRUZLOMA-1.jpg'},
    {'name':'VINO_ESP_MARQUES_DE_PLATA_BOBAL.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/06/MARQUES-DE-PLATA-BOBAL-750ml.png'},
    {'name':'COGNAC_HENNESSY_VS.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2022/04/COGNAC-HENNESSY-V.png'},
    {'name':'VINO_ESP_CLIO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/05/CLIO-750ml.png'},
    {'name':'CAVA_VILLA_CONCHI_BRUT_BLUSH.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/CAVA-VILLA-CONCHI-BRUT-BLUSH-750ml.png'},
    {'name':'VINO_ESP_PAZO_CILLEIRO_ALBARINO_DO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/02/PAZO-CILLEIRO-ALBARINO-D.O..jpg'},
    {'name':'RON_FLOR_DE_CANA_18_A.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2020/04/FLOR-DE-CANA-18.png'},
    {'name':'VINO_EU_HOPE_FAMILY_WINE_AUSTIN_HOPE_CAB_SAUV.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/HOPE-FAMILY-WINE-AUSTIN-HOPE-CAB-SAUV-750ml.png'},
    {'name':'VINO_TINTO_DARK_RED_DIABLO.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/08/DIABLO-DARK-RED-600x600-1.jpg'},
    {'name':'VINO_ESPUMOSO_ICE_DEMISEC.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/09/VEUVE-DU-VERNAY-ICE.jpg'},
    {'name':'VINO_ITA_PLANETA_CHARDONNAY.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/06/PLANETA-CHARDONNAY.png'},
    {'name':'PACK_VINA_ALBALI__RESERVA_REGALA_CASA_ALBALI_TEMPRANILLOSHIRAZ.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/PACK-ALBALI-RESV-REGALA-ALBALI-TEMPRANILLO-SHIRAZ.png'},
    {'name':'VINO_ESP_JOTA_DE_TORO_VINAS_VIEJAS_CRIANZA.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/07/JOTA-DE-TORO-VINAS-VIEJAS-CRIANZA-750ml.png'},
    {'name':'WHISKY_BUCHANANS_MASTER.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2023/05/WHISKY-BUCHANANS-MASTER-750ml.png'},
    {'name':'VINO_ESPUMOSO_ICE_DEMISEC_200ML.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2021/09/VEUVE-ICE-200ML.png'},
    {'name':'VINO_ESP_FAUSTINO_CRIANZA.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2018/02/FAUSTINO-CRIANZA.jpg'},
    {'name':'GB_QUESO_MANCHEGO_SEMICURADO_150gr.jpg','url':'https://laguarda.com.ec/wp-content/uploads/2021/08/QUESO-MANCHEGO.png'},
]

# Carpeta de destino para las imágenes descargadas
destination_folder = "img_urls"

# Crear la carpeta de destino si no existe
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Descargar las imágenes
for image in image_urls:
    response = requests.get(image['url'])
    if response.status_code == 200:
        image_name = os.path.basename(image['name'])
        image_path = os.path.join(destination_folder, image_name)
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Imagen {image_name} descargada correctamente.")
    else:
        print(f"No se pudo descargar la imagen desde {image['url']}")

print("Todas las imágenes han sido descargadas.")
