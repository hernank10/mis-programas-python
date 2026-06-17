#!/usr/bin/env python3
"""Script de prueba para verificar la integración SQL"""

from db_manager import db

print("=" * 50)
print("  🧪 PRUEBA DE INTEGRACIÓN SQL")
print("=" * 50)

# Probar conexión
print("\n📊 Tablas existentes:")
tablas = db.consultar("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
for t in tablas:
    count = db.consultar_uno(f"SELECT COUNT(*) FROM {t[0]}")[0]
    print(f"  • {t[0]}: {count} registros")

# Probar usuarios
print("\n👥 Usuarios:")
usuarios = db.consultar("SELECT username, rol FROM usuarios")
for u in usuarios:
    print(f"  • {u['username']} ({u['rol']})")

# Probar declinaciones
print("\n🏛️ Declinaciones latinas:")
declinaciones = db.consultar("SELECT palabra, declinacion FROM declinaciones")
for d in declinaciones:
    print(f"  • {d['palabra']} ({d['declinacion']}ª)")

print("\n✅ Prueba completada")
