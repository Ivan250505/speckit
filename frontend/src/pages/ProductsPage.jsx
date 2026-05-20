import React, {useState} from 'react'
import ProductsTable from '../components/ProductsTable'
import ModalForm from '../components/ModalForm'
import ProductForm from '../components/ProductForm'

export default function ProductsPage(){
  const [isOpen, setIsOpen] = useState(false)
  const [refreshKey, setRefreshKey] = useState(0)

  const handleCreated = () => {
    setIsOpen(false)
    setRefreshKey((value) => value + 1)
  }

  return (
    <div>
      <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-6 gap-4">
        <div>
          <h1 className="text-2xl font-semibold">Productos</h1>
          <p className="text-sm text-gray-500">Administra los productos y agrega nuevos registros.</p>
        </div>
        <button
          type="button"
          onClick={() => setIsOpen(true)}
          className="inline-flex items-center justify-center rounded bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
        >
          Agregar producto
        </button>
      </div>
      <ProductsTable refreshKey={refreshKey} />
      <ModalForm open={isOpen} title="Agregar producto" onClose={() => setIsOpen(false)}>
        <ProductForm onCreated={handleCreated} onCancel={() => setIsOpen(false)} />
      </ModalForm>
    </div>
  )
}
