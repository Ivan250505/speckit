import React, {useState, useEffect} from 'react'

export default function SearchBar({value='', onChange}){
  const [q, setQ] = useState(value)
  useEffect(()=>{
    const id = setTimeout(()=> onChange && onChange(q), 300)
    return ()=> clearTimeout(id)
  },[q,onChange])

  return (
    <div className="flex items-center space-x-2">
      <input value={q} onChange={e=>setQ(e.target.value)} placeholder="Buscar por nombre..." className="border rounded px-3 py-2 w-full" />
      {q && <button onClick={()=>setQ('')} className="text-sm text-gray-600">Limpiar</button>}
    </div>
  )
}
