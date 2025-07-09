# 🔗 TrustlessChain – Mini Blockchain Educativa en Python

**TrustlessChain** es una implementación simple y educativa de una blockchain sin minería, centrada en la integridad, verificabilidad y descentralización, construida desde cero con Python.

> 📚 Diseñado para practicar estructuras de datos (listas enlazadas, árboles binarios, colas, pilas), hashing y conceptos base de Web3.

---

## 🚀 Features

- ✅ **Transacciones** con serialización determinista y hashing propio.
- ✅ **Árbol Merkle** desde cero para garantizar integridad de transacciones.
- ✅ **Bloques** que agrupan transacciones y se encadenan con hashes.
- ✅ **Blockchain** como lista enlazada validable.
- ✅ **Validación completa de la cadena**: detección de alteraciones.
- ✅ **Sin librerías externas** (salvo `hashlib` y `time`).

---

## 🧠 Estructuras implementadas a mano

| Estructura         | Uso en el proyecto                                 |
|--------------------|----------------------------------------------------|
| Árbol binario      | Árbol Merkle (hashes de transacciones)             |
| Lista enlazada     | Blockchain (cada bloque apunta al anterior)        |
| Pila / Cola        | (próximo objetivo: historial o transacciones en espera) |
| Hashing            | Hash de transacciones, bloques y árboles Merkle    |

---

## 📦 Cómo usar

### 1. Clonar el proyecto
```bash
git clone https://github.com/tuusuario/trustlesschain.git
cd trustlesschain
```

### 2. Ejecutar los tests
```sh
python main.py  # o test.py, según como lo tengas estructurado
```

Todos los tests corren automáticamente y verifican:

- Transacciones consistentes
- Árbol Merkle funcional
- Bloques correctos
- Integridad de la blockchain

## 🧪 Ejemplo de uso

```python
from blockchain.Transaction import Transaction
from blockchain.Blockchain import Blockchain

t1 = Transaction("alice", "bob", 100)
t2 = Transaction("bob", "carol", 50)

blockchain = Blockchain()
blockchain.add_block([t1, t2])

print("Cadena válida:", blockchain.is_chain_valid())
```
---

## 🧱 Estructura del proyecto
```bash
📁 trustlesschain/
├── transaction.py     # Clase Transaction
├── merkletree.py      # Árbol Merkle hecho a mano
├── block.py           # Clase Block
├── blockchain.py      # Clase Blockchain (lista enlazada)
├── test.py            # Tests automáticos
└── README.md
```
---

## 🛠️ Roadmap (cosas por hacer)

- [ ] 🌳 Verificación de pertenencia con Merkle Proof
- [ ] 🌐 Simulación de nodos P2P con copias locales de la blockchain
- [ ] 🧠 Protocolo de consenso simple
- [ ] 💾 Guardar/leer bloques desde disco
- [ ] 📲 CLI interactiva para enviar transacciones

---

## 🎯 Objetivos del proyecto

Este proyecto nace del interés por aprender cómo funciona una blockchain desde adentro, sin depender de librerías externas ni frameworks. La idea es entender a fondo:

- Cómo se valida la información en sistemas distribuidos.
- Por qué el hashing es fundamental para la seguridad.
- Cómo usar estructuras clásicas (árboles, listas, colas) en contextos modernos como Web3.

---

## 🧑‍💻 Autor
Mateo Díaz – Estudiante de Ingeniería Informática