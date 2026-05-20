import React from 'react'

export default function Table({columns = [], data = [], rowKey = 'id', className = ''}){
  return (
    <div className={className}>
      <table className="min-w-full border-collapse">
        <thead>
          <tr className="text-left border-b">
            {columns.map(col => (
              <th key={col.key} className="py-2 px-3">{col.title}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map(row => (
            <tr key={row[rowKey]} className={`${row.cantidad < 5 ? 'bg-yellow-50' : ''} border-b` }>
              {columns.map(col => (
                <td key={col.key} className="py-2 px-3">{col.render ? col.render(row) : row[col.key]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
