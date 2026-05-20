# Feature Specification: Gestión de Inventario

**Feature Branch**: `001-gestion-inventario`

**Created**: 2026-05-17

**Status**: Draft

**Input**: User description: "Quiero construir un sistema de gestión de inventario con las siguientes características:

- CRUD completo de productos (crear, ver, editar, eliminar)
- Cada producto tiene: nombre, categoría, cantidad, precio y descripción
- Tabla principal con búsqueda y filtro por categoría
- Alerta visual cuando el stock sea menor a 5 unidades
- Panel resumen con total de productos y valor total del inventario
- Exportar inventario a CSV
- Interfaz moderna y responsiva
- Backend con FastAPI y base de datos SQLite
- Frontend con React y Tailwind CSSv"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Gestionar productos (Priority: P1)

Como usuario administrador, quiero crear, ver, editar y eliminar productos para mantener el inventario actualizado.

**Why this priority**: Es la funcionalidad esencial para operar el inventario.

**Independent Test**: Crear un producto nuevo, editar su cantidad y eliminarlo; verificar resultados en la interfaz y en la exportación CSV.

**Acceptance Scenarios**:

1. **Given** que estoy en la vista de productos, **When** selecciono "Crear producto" y completo los campos válidos, **Then** el producto aparece en la tabla y en el resumen.
2. **Given** un producto existente, **When** edito nombre/categoría/cantidad/precio/descripción y guardo, **Then** los cambios se muestran inmediatamente.
3. **Given** un producto existente, **When** lo elimino, **Then** desaparece de la tabla y el resumen se actualiza.

---

### User Story 2 - Buscar y filtrar (Priority: P1)

Como usuario, quiero buscar por nombre y filtrar por categoría para encontrar productos rápidamente.

**Why this priority**: Mejora eficiencia en la gestión diaria.

**Independent Test**: Usar la barra de búsqueda y el filtro por categoría para reducir la lista y verificar que los resultados sean correctos.

**Acceptance Scenarios**:

1. **Given** muchos productos, **When** escribo parte del nombre en la búsqueda, **Then** la tabla muestra solo coincidencias.
2. **Given** varias categorías, **When** aplico un filtro, **Then** la tabla muestra solo productos de esa categoría.

---

### User Story 3 - Alertas de stock bajo (Priority: P1)

Como usuario, quiero ver una alerta visual cuando la cantidad sea menor a 5 unidades para reordenar stock oportunamente.

**Why this priority**: Previene quiebres de stock.

**Independent Test**: Crear o editar un producto con cantidad < 5 y verificar la alerta visual en la fila y en el panel resumen.

**Acceptance Scenarios**:

1. **Given** un producto con cantidad = 4, **When** se muestra la tabla, **Then** la fila tiene un estado destacado (color/ícono) y el resumen indica productos con stock bajo.

---

### User Story 4 - Panel resumen y exportación (Priority: P2)

Como usuario, quiero ver el total de productos y el valor total del inventario y poder exportarlo a CSV para reportes.

**Why this priority**: Facilita análisis y continuidad de negocio.

**Independent Test**: Ver el panel resumen y exportar CSV; abrir CSV y comprobar columnas y valores.

**Acceptance Scenarios**:

1. **Given** productos en la base de datos, **When** visito la vista principal, **Then** el panel muestra el recuento total y el valor total (suma de cantidad*precio).
2. **Given** datos visibles, **When** clic en "Exportar CSV", **Then** se descarga un CSV con columnas: id,nombre,categoría,cantidad,precio,descripción,valor_total_por_producto.

---

### Edge Cases

- Producto con cantidad negativa o no entera — UI debe validar e impedir valores inválidos.
- Precio con formato inválido — validar input de moneda.
- Eliminación de producto referenciado en procesos externos — sistema debe permitir solo si no hay dependencias (fuera de alcance para v1 si no existen procesos externos).
- CSV con caracteres especiales/acentos — exportar en UTF-8.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El sistema MUST permitir crear productos con los atributos: nombre, categoría, cantidad, precio y descripción.
- **FR-002**: El sistema MUST permitir ver la lista de productos en una tabla principal con paginación o scroll infinito.
- **FR-003**: El sistema MUST permitir editar y eliminar productos desde la interfaz.
- **FR-004**: La tabla MUST soportar búsqueda por nombre (texto parcial) y filtro por categoría.
- **FR-005**: El sistema MUST mostrar una alerta visual en la fila del producto y en el panel resumen cuando `cantidad < 5`.
- **FR-006**: El sistema MUST mostrar un panel resumen con: total de productos (conteo) y valor total del inventario (sumatoria de `cantidad * precio`).
- **FR-007**: El sistema MUST permitir exportar el inventario visible a un archivo CSV con columnas mínimas: id,nombre,categoría,cantidad,precio,descripción,valor_total_por_producto.
- **FR-008**: La interfaz MUST ser responsiva y tener una apariencia moderna.
- **FR-009**: El backend MUST exponer API REST para las operaciones CRUD y endpoints para búsqueda/filtrado y exportación.
- **FR-010**: La persistencia MUST usar una base de datos relacional ligera (SQLite) para v1.

### Key Entities

- **Producto**: id, nombre, categoría, cantidad (entero), precio (decimal), descripción, creado_at, actualizado_at.
- **Categoría**: id, nombre.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Un administrador puede crear y listar 100 productos en menos de 2 minutos.
- **SC-002**: La función de búsqueda devuelve resultados relevantes para los términos más comunes en menos de 1 segundo (percepción de rapidez).
- **SC-003**: Las alertas de stock bajo se muestran correctamente para productos con `cantidad < 5` en el 100% de los casos.
- **SC-004**: La exportación CSV incluye todas las filas visibles y se descarga correctamente en UTF-8.

## Assumptions

- La moneda por defecto será la moneda local del usuario; los precios se almacenan como decimal, sin convertir moneda.
- Autenticación/roles no son parte de v1; se asume acceso por usuario administrativo en un entorno protegido.
- Integraciones externas para reabastecimiento quedan fuera del alcance de v1.
- Soporte multiusuario y concurrencia básica de SQLite es suficiente para MVP.
