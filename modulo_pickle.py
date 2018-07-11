from pickle import *

def pasa_dic():
	palabras={}
	palabras["ARBOL"]="Hay quien bebe por la boca, que es la forma de beber, pero sé de alguien que bebe solamente por los pies."
	palabras["CASA"]="Vivo dentro de ella y el caracol también. Él la lleva a cuesta y yo nunca podré."
	palabras["SILLA"]="Con patas y espalda, no se mueve ni anda."
	palabras["AUDIO"]="Puedes escucharme pero no me sientes, necesito siempre de mi amigo sonido"
	palabras["VENTANA"]="Es venta y no se vende, es Ana, pero no es gente."
	palabras["COMPUTADORA"]="Tiene pantalla y no es un TV, tambien teclas y no es control remoto, posee ventilación y no es aire acondicionado"
	palabras["RELOJ"]="En un castillo redondo, doce cabelleros de guardia están; un flaco lancero y un gordo escudero marchan al compás."
	palabras["AVION"]="Ave de hierro y acero canta con fuerte zumbido, no tiene plumas ni pico y el cobertizo es su nido."
	palabras["MILANESA"]="Puede ser mi interior filete de carne y pollo pero siempre empapado estoy."
	palabras["ALMOHADA"]="Aunque al dormir me consultan, nunca suelo contestar."
	palabras["DICCIONARIO"]="Todas las palabras sé y, aunque todas las explico, nuncá las pronunciaré."
	palabras["CUCHARA"]="Sube llena, baja vacía, y si no se da prisa, la sopa se enfría."
	palabras["TIEMPO"]="Corre más que un ciclista, nunca da marcha atrás, si lo pierdes de vista, ¡Cómo envejecerás!."
	palabras["GASOLINERO"]="No soy bombero, pero tengo manguera y alimento a los coches por la carretera."
	palabras["CARTA"]="Cruza los ríos, tambien los mares, vuela sin alas a todas partes."
	palabras["PINCEL"]="Aunque no soy importante, en la vida pinto algo; mas no podré trabajar cuando yo me quede calvo."
	palabras["VIENTO"]="Vuela sin alas, silba sin boca, azota sin manos y tú ni lo ves ni lo tocas."
	palabras["CASCADA"]="Es algo que siempre cae, y nunca se rompe."
	palabras["HORIZONTE"]="El cielo y la tierra se van a juntar; la ola y la nube se van a enredar. Vayas donde vayas siempre lo verás, por mucho que andes nunca llegarás"
	palabras["HIELO"]="Soy duro y bastante frío, cuando me tocas me sonrojo y si ahorita me vez, al rato, solo te mojo."
	palabras["OXIGENO"]="Me ves, pero no me ves, me respiras, y no tengo olor, no soy ni el aire ni el viento."
	palabras["ABECEDARIO"]="Es una palabra que tiene cinco sílabas y más de veinte letras."
	palabras["MAÑANA"]="Una cosa que no ha sido y tiene que ser, y que cuando sea dejara de ser."
	palabras["SIERRA"]="Cuando me observas de lado, parezco una cordillera, el don que me fue otorgado es dar forma a la madera."
	palabras["NUEVE"]="Es un número que vale menos si lo ponemos al revés."
	palabras["PIOJO"]="Es un animal que tiene los pies en la cabeza."
	palabras["HUELLAS"]="Cuando iba, fui con ellas. Y cuando volví, me encontré con ellas."
	palabras["CEREBRO"]="Ordenes da, ordenes recibe, algunas autoriza, otras prohíbe."
	palabras["HUEVO"]="Una caja pequeñita, blanquita como la cal, todos la saben abrir, nadie la sabe cerrar."
	palabras["OSCURIDAD"]="Si no hay, se ve. Si hay poca, se ve. Si hay mucho, no se ve."
	palabras["PIOJO"]="Es un animal que tiene los pies en la cabeza."
	palabras["ECO"]="Sabe responder cualquier pregunta y en cualquier idioma."
	palabras["HUMO"]="Alto, alto como un pino y pesa menos que un comino."
	palabras["CARBON"]="Es negro cuando lo comprás, rojo cuando se usa y gris cuando se tira."
	palabras["PEINE"]="Tiene dientes pero no come nunca."
	palabras["ALFILER"]="Mi nombre empieza con A, de las damas muy querido, si me prende voy seguro, y si me sueltan, perdido."
	palabras["MONEDA"]="Tiene cara no tiene cuerpo."
	palabras["SANDIA"]="Tiene saco verde, usa chaleco colorado, además botones negros."
	palabras["ESTRELLAS"]="Un platito de avellanas, de día se recojen y de noche se desparrama."
	palabras["ACEITE"]="En verdes ramas nací, en molino me estrujaron, en pozo me metí, y del pozo me sacaron a la cocina a freír."
	palabras["KARATE"]="Tengo llaves pero no cerradura. El blanco y el negro pasan por mi cintura."
	palabras["FELPUDO"]="En la puerta está quietito pero no entra ni un poquito."
	palabras["FAROLA"]="Soy alta, mi cabeza brillante y siempre guío a los caminantes."
	palabras["BACALAO"]="Una vaca de lado, que resultó pescado."
	palabras["PIÑA"]="Tiene ojos y no ve, posee corona y no es rey, tiene escamas sin ser pez."
	palabras["CABALLO"]="Es un animal muy elegante, muy veloz y poco fiero; y cuando quiero calzarme voy a casa del herrero."
	palabras["ABEJA"]="De celda en celda voy pero presa no estoy."
	palabras["HORMIGA"]="Cargadas van, cargadas vienen y en el camino no se detienen."
	palabras["CARACOL"]="Un solo portero, un solo inquilino, tu casa redonda la llevas contigo."
	palabras["OVEJA"]="Puñadito de algodón que brinca sin ton ni son."
	palabras["LAGARTIJA"]="Porque tengo sangre fría aparezco en primavera en piedras encaramada siempre al sol que más calienta."
	palabras["HIPOPÓTAMO"]="Tengo hipo al decir mi nombre."
	palabras["SASTRE"]="Con destreza y sin desatre hace las mangas al traje."
	palabras["CARTERO"]="Por las calles viene y va, reparte noticias, ya está por acá."
	palabras["PINTOR"]="Brocha y pincel va siempre con él."
	palabras["TRIGO"]="Verde me crié, rubio me cortaron, rojo me molieron, blanco me amasaron."
	palabras["PLATANO"]="Oro parece, plata no es. Abre las cortinas y verás lo que es."
	


	pickle_file = open('palabras.pickle', 'wb')
	dump(palabras, pickle_file)

	pickle_file = open('palabras.pickle','rb')
	contenido_dic = load(pickle_file)

	return contenido_dic