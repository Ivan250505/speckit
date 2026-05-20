import React, {useEffect} from 'react'

export default function ModalForm({open, title, children, onClose}){
  useEffect(()=>{
    function onKey(e){ if(e.key === 'Escape') onClose && onClose() }
    if(open) window.addEventListener('keydown', onKey)
    return ()=> window.removeEventListener('keydown', onKey)
  },[open,onClose])

  if(!open) return null
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div className="fixed inset-0 bg-black opacity-40" onClick={onClose}></div>
      <div className="bg-white rounded-lg shadow-lg p-6 z-10 w-full max-w-xl">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold">{title}</h3>
          <button onClick={onClose} aria-label="Cerrar" className="text-gray-600">✕</button>
        </div>
        <div>{children}</div>
      </div>
    </div>
  )
}
