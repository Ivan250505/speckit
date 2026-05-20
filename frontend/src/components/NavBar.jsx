import React from 'react'
import { NavLink } from 'react-router-dom'

const activeClass = 'bg-blue-600 text-white'
const inactiveClass = 'text-sm px-3 py-1 rounded hover:bg-gray-100'

export default function NavBar(){
  return (
    <nav className="bg-white shadow px-4 py-3 flex items-center justify-between">
      <div className="flex items-center space-x-3">
        <div className="text-2xl font-bold">🔷</div>
        <div>
          <div className="text-lg font-semibold">Gestión de Inventario</div>
          <div className="text-sm text-gray-500">Panel administrativo</div>
        </div>
      </div>
      <div className="flex items-center space-x-4">
        <NavLink to="/" className={({isActive}) => `${inactiveClass} ${isActive ? activeClass : ''}`}>
          Inicio
        </NavLink>
        <NavLink to="/products" className={({isActive}) => `${inactiveClass} ${isActive ? activeClass : ''}`}>
          Productos
        </NavLink>
        <NavLink to="/categories" className={({isActive}) => `${inactiveClass} ${isActive ? activeClass : ''}`}>
          Categorías
        </NavLink>
        <a
          href="http://127.0.0.1:8000/api/v1/products/export"
          target="_blank"
          rel="noreferrer"
          className="text-sm px-3 py-1 rounded hover:bg-gray-100"
        >
          Exportar
        </a>
      </div>
    </nav>
  )
}
