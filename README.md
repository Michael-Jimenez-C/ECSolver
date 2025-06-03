# 📊 Excel Solver - Proyecto del Curso

## 📝 Descripción del Proyecto

Este proyecto tiene como objetivo implementar un solver de ecuaciones básico para hojas de cálculo utilizando Python. Se desarrollará una aplicación que permita resolver ecuaciones matemáticas en el contexto de un excel, evaluando fórmulas y dependencias entre celdas.

### 🎯 Objetivos de Aprendizaje

- Implementar algoritmos de resolución de ecuaciones en Python
- Trabajar con metodologías de desarrollo colaborativo (Git/GitHub)
- Aplicar principios de modularidad en Python

---

## 🏗️ Estructura del Proyecto

```
excel-solver/
├── src/
│   └── solver/
│       ├── solver.py        # Lógica principal y entrada
│
├── /tests/                  
│   ├── test.py
├── pyproject.toml         # Configuración del paquete
├── README.md              # Este archivo
└── .gitignore             # Archivos a ignorar
```

---

## ⚡ Funcionalidades del Proyecto

- [x] **Parser de fórmulas**: Analizar y parsear ecuaciones de celdas
- [x] **Evaluador de expresiones**: Resolver operaciones matemáticas básicas
- [x] **Gestión de dependencias**: Identificar relaciones entre celdas
- [ ] **Solver iterativo**: Resolver sistemas de ecuaciones
- [x] **Mostrar resultados**: Visualizar soluciones por consola
- [ ] **Validación de entrada**: Verificar formato de ecuaciones

---

## 🚀 Cómo Empezar

### 1. Clonar el Repositorio

```bash
git clone https://github.com/ACMUD/ECSolver
cd excel-solver
```

### 2. Configurar el Entorno

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\\Scripts\\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## 💻 Metodología de Trabajo

### 🔄 Flujo de Trabajo con Git

1. **Crear una rama** para cada nueva funcionalidad:
   ```bash
   git checkout -b feature/nombre-funcionalidad
   ```

2. **Realizar commits** pequeños y descriptivos:
   ```bash
   git add .
   git commit -m \"feat: implementar parser de fórmulas básico\"
   ```

3. **Subir la rama** al repositorio remoto:
   ```bash
   git push origin feature/nombre-funcionalidad
   ```

4. **Crear Pull Request** en GitHub para revisión

### 📝 Convención de Commits

Seguimos el estándar de [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` nueva funcionalidad
- `fix:` corrección de errores
- `docs:` cambios en documentación
- `test:` agregar o modificar tests
- `refactor:` refactorización de código

**Ejemplos:**
```
feat: agregar evaluador de expresiones matemáticas
fix: corregir error en detección de dependencias circulares
docs: actualizar README con ejemplos de uso
test: agregar tests para clase Solver
```

### 🌿 Estrategia de Ramas

- `main`: rama principal (código estable)
- `develop`: rama de desarrollo (integración)
- `feature/`: ramas para nuevas funcionalidades

### 📋 Pull Requests

Cada PR debe incluir:

1. **Descripción clara** de los cambios realizados
2. **Documentación** actualizada si es necesario
3. **Revisión** de al menos un compañero

#### Template para PR:

```markdown
## Descripción
Breve descripción de los cambios realizados.

## Tipo de cambio
- [ ] Nueva funcionalidad
- [ ] Corrección de error
- [ ] Refactorización
- [ ] Actualización de documentación

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He realizado una auto-revisión
- [ ] He comentado el código en áreas complejas
- [ ] Mis cambios no generan nuevas advertencias
```

---

### 💡 Consejos para Contribuir:

- Leer el código existente antes de empezar
- Mantener tus PRs pequeños y enfocados
- Documentar funciones complejas
- Pedir ayuda si hay complicaciones


## 📚 Recursos Adicionales

### Documentación Oficial:
- [Python ast](https://docs.python.org/3/library/ast.html)
- [NumPy](https://numpy.org/doc/stable/)
- [Git Documentation](https://git-scm.com/doc)


## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.


*¡Happy coding! 🐍📊*
