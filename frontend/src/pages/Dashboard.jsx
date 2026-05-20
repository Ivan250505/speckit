import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Package, DollarSign, AlertTriangle, Plus, Tag, Download } from 'lucide-react'
import api from '../services/api'

export default function Dashboard() {
  const navigate = useNavigate()
  const [summary, setSummary] = useState({ total_count: 0, total_value: 0, low_stock_count: 0 })
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.get('/products/summary')
      .then(r => setSummary(r.data))
      .catch(() => setSummary({ total_count: 0, total_value: 0, low_stock_count: 0 }))
      .finally(() => setLoading(false))
  }, [])

  const StatCard = ({ icon: Icon, title, value, color, bgColor }) => (
    <div className={`${bgColor} rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow`}>
      <div className="flex items-center justify-between">
        <div>
          <p className="text-gray-600 text-sm font-medium mb-2">{title}</p>
          <p className="text-4xl font-bold text-gray-900">{value}</p>
        </div>
        <div className={`${color} p-4 rounded-xl`}>
          <Icon size={32} className="text-white" />
        </div>
      </div>
    </div>
  )

  const QuickAccessBtn = ({ icon: Icon, label, onClick, color }) => (
    <button
      onClick={onClick}
      className={`${color} text-white px-6 py-3 rounded-xl font-semibold flex items-center gap-2 hover:shadow-lg transition-all hover:scale-105`}
    >
      <Icon size={20} />
      {label}
    </button>
  )

  return (
    <div className="w-full">
      {/* HERO SECTION */}
      <section className="bg-gradient-to-r from-blue-900 via-blue-800 to-blue-700 rounded-3xl p-12 mb-12 text-white shadow-2xl">
        <h1 className="text-5xl font-bold mb-4">
          Sistema de Gestión de Inventario
        </h1>
        <p className="text-xl text-blue-100 mb-8 max-w-2xl">
          Controla tu inventario de forma sencilla y eficiente. Gestiona productos, categorías y mantén un control total del stock.
        </p>
        <button
          onClick={() => navigate('/products')}
          className="bg-white text-blue-900 px-8 py-4 rounded-xl font-bold text-lg hover:bg-blue-50 transition-all hover:shadow-lg"
        >
          Ver Inventario →
        </button>
      </section>

      {/* RESUMEN DE ESTADÍSTICAS */}
      <section className="mb-12">
        <h2 className="text-3xl font-bold text-gray-900 mb-8">Resumen General</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <StatCard
            icon={Package}
            title="Total de Productos"
            value={summary.total_count}
            color="bg-blue-500"
            bgColor="bg-blue-50"
          />
          <StatCard
            icon={DollarSign}
            title="Valor Total del Inventario"
            value={`$${summary.total_value.toLocaleString()}`}
            color="bg-green-500"
            bgColor="bg-green-50"
          />
          <StatCard
            icon={AlertTriangle}
            title="Productos con Stock Bajo"
            value={summary.low_stock_count}
            color={summary.low_stock_count > 0 ? "bg-red-500" : "bg-orange-500"}
            bgColor={summary.low_stock_count > 0 ? "bg-red-50" : "bg-orange-50"}
          />
        </div>
      </section>

      {/* ACCESOS RÁPIDOS */}
      <section>
        <h2 className="text-3xl font-bold text-gray-900 mb-8">Accesos Rápidos</h2>
        <div className="bg-white rounded-2xl p-8 shadow-lg">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <QuickAccessBtn
              icon={Plus}
              label="Agregar Producto"
              onClick={() => navigate('/products')}
              color="bg-gradient-to-r from-blue-500 to-blue-600"
            />
            <QuickAccessBtn
              icon={Tag}
              label="Ver Categorías"
              onClick={() => navigate('/categories')}
              color="bg-gradient-to-r from-purple-500 to-purple-600"
            />
            <QuickAccessBtn
              icon={Download}
              label="Exportar CSV"
              onClick={() => {
                api.get('/products/export', { responseType: 'blob' })
                  .then(r => {
                    const url = URL.createObjectURL(r.data)
                    const a = document.createElement('a')
                    a.href = url
                    const match = /filename="?([^"]+)"?/.exec(r.headers['content-disposition'] || '')
                    a.download = match ? match[1] : 'productos.csv'
                    document.body.appendChild(a)
                    a.click()
                    a.remove()
                    URL.revokeObjectURL(url)
                  })
                  .catch(() => alert('Error al exportar'))
              }}
              color="bg-gradient-to-r from-green-500 to-green-600"
            />
          </div>
        </div>
      </section>
    </div>
  )
}
