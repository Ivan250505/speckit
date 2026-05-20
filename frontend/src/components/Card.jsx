import React from 'react'

export default function Card({title, children, className = '', actions}){
  return (
    <div className={`bg-white rounded-lg shadow p-4 ${className}`}>
      {title && <div className="flex items-center justify-between mb-3">
        <h3 className="text-lg font-semibold">{title}</h3>
        {actions}
      </div>}
      <div>{children}</div>
    </div>
  )
}
