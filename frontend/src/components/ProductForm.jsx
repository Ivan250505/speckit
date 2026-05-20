import React, {useEffect, useState} from 'react'
import api from '../services/api'

export default function ProductForm({onCreated, onCancel}){
  const [categories, setCategories] = useState([])
  const [form, setForm] = useState({
    nombre: '',
    categoria_id: '',
    cantidad: 0,
    precio: 0.0,
    descripcion: '',
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(()=>{
    api.get('/categories')
      .then(r => setCategories(Array.isArray(r.data) ? r.data : []))
      .catch(()=> setCategories([]))
  },[])

  const handleChange = (field) => (event) => {
    const value = field === 'categoria_id'
      ? (event.target.value ? Number(event.target.value) : '')
      : event.target.value

    setForm((prev) => ({ ...prev, [field]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setLoading(true)
    setError('')

    try {
      await api.post('/products', {
        nombre: form.nombre,
        categoria_id: form.categoria_id || null,
        cantidad: Number(form.cantidad),
        precio: Number(form.precio),
        descripcion: form.descripcion || null,
      })
      setForm({ nombre: '', categoria_id: '', cantidad: 0, precio: 0.0, descripcion: '' })
      onCreated && onCreated()
    } catch (err) {
      setError('No se pudo crear el producto. Intenta de nuevo.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="grid grid-cols-1 gap-4">
        <label className="block">
          <span className="text-sm font-medium text-gray-700">Nombre</span>
          <input
            type="text"
            value={form.nombre}
            onChange={handleChange('nombre')}
            required
            className="mt-1 w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          />
        </label>
        <label className="block">
          <span className="text-sm font-medium text-gray-700">Categoría</span>
          <select
            value={form.categoria_id}
            onChange={handleChange('categoria_id')}
            className="mt-1 w-full rounded border-gray-300 bg-white shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="">Sin categoría</option>
            {categories.map((category) => (
              <option key={category.id} value={category.id}>{category.nombre}</option>
            ))}
          </select>
        </label>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <label className="block">
            <span className="text-sm font-medium text-gray-700">Cantidad</span>
            <input
              type="number"
              min="0"
              value={form.cantidad}
              onChange={handleChange('cantidad')}
              required
              className="mt-1 w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </label>
          <label className="block">
            <span className="text-sm font-medium text-gray-700">Precio</span>
            <input
              type="number"
              min="0"
              step="0.01"
              value={form.precio}
              onChange={handleChange('precio')}
              required
              className="mt-1 w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </label>
        </div>
        <label className="block">
          <span className="text-sm font-medium text-gray-700">Descripción</span>
          <textarea
            value={form.descripcion}
            onChange={handleChange('descripcion')}
            rows="3"
            className="mt-1 w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          />
        </label>
      </div>
      {error && <div className="mt-3 text-sm text-red-600">{error}</div>}
      <div className="mt-4 flex justify-end gap-3">
        <button
          type="button"
          onClick={onCancel}
          className="rounded border border-gray-300 px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
        >
          Cancelar
        </button>
        <button
          type="submit"
          disabled={loading}
          className="rounded bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? 'Guardando...' : 'Guardar producto'}
        </button>
      </div>
    </form>
  )
}
