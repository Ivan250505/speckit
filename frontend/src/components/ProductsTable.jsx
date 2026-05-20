import React, {useEffect, useState} from 'react'
import api from '../services/api'

export default function ProductsTable({refreshKey = 0}){
  const [products, setProducts] = useState([])

  useEffect(()=>{
    api.get('/products')
      .then(r => setProducts(Array.isArray(r.data) ? r.data : []))
      .catch(() => setProducts([]))
  },[refreshKey])

  const productList = Array.isArray(products) ? products : []

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-lg font-medium mb-4">Productos</h2>
      <table className="min-w-full text-left">
        <thead>
          <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Cantidad</th>
            <th>Precio</th>
          </tr>
        </thead>
        <tbody>
          {productList.length === 0 ? (
            <tr>
              <td colSpan="4" className="px-4 py-6 text-center text-gray-500">No hay productos registrados.</td>
            </tr>
          ) : productList.map(p=> (
            <tr key={p.id} className={p.cantidad < 5 ? 'bg-yellow-50' : ''}>
              <td>{p.id}</td>
              <td>{p.nombre}</td>
              <td>{p.cantidad}</td>
              <td>{p.precio}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
