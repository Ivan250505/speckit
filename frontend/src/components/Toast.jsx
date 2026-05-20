import React, {createContext, useContext, useState, useCallback} from 'react'

const ToastContext = createContext(null)

export function useToast(){ return useContext(ToastContext) }

export function ToastProvider({children}){
  const [toasts, setToasts] = useState([])
  const push = useCallback((msg, type='info')=>{
    const id = Date.now()
    setToasts(t=>[...t, {id,msg,type}])
    setTimeout(()=> setToasts(t=> t.filter(x=>x.id!==id)), 4000)
  },[])
  const value = {push}

  return (
    <ToastContext.Provider value={value}>
      {children}
      <div className="fixed top-4 right-4 space-y-2 z-50">
        {toasts.map(t=> (
          <div key={t.id} className={`px-4 py-2 rounded shadow ${t.type==='error'? 'bg-red-100 text-red-800' : t.type==='success'? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
            {t.msg}
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  )
}

export default ToastProvider
