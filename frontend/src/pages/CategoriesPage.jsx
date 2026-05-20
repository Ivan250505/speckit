import React, {useEffect, useState} from 'react'
import api from '../services/api'

export default function CategoriesPage(){
  const [categories, setCategories] = useState([])

  useEffect(()=>{
    api.get('/categories')
      .then(r => setCategories(Array.isArray(r.data) ? r.data : []))
      .catch(()=> setCategories([]))
  },[])

  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <div>
          <h1 className="text-2xl font-semibold">Categorías</h1>
          <p className="text-sm text-gray-500">Lista de categorías disponibles en inventario.</p>
        </div>
      </div>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="min-w-full text-left">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3">Id</th>
              <th className="px-4 py-3">Nombre</th>
            </tr>
          </thead>
          <tbody>
            {categories.length === 0 ? (
              <tr>
                <td colSpan="2" className="px-4 py-6 text-center text-gray-500">No hay categorías disponibles.</td>
              </tr>
            ) : categories.map(cat => (
              <tr key={cat.id} className="border-t">
                <td className="px-4 py-3">{cat.id}</td>
                <td className="px-4 py-3">{cat.nombre}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
