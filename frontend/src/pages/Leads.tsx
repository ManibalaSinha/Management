import React, { useEffect, useState } from 'react';
import API from '../api';

export default function Leads(){
   const [leads, setLeads] = useState<any[]>([]);
   const [q, setQ] = useState('');
   const fetchLeads = async ()=>{
      const res = await API.get('/leads', { params: { q } });
      setLeads(res.data);
}
useEffect(()=>{ fetchLeads(); }, [q]);
return (
   <div style={{padding:20}}>
      <h2>Leads</h2>
      <input placeholder='search' value={q} onChange={e=>setQ(e.target.value)} />
   <table>
      <thead><tr><th>ID</th><th>Name</th><th>Email</th><th>Risk</th></tr></thead>
      <tbody>
      {leads.map(l=> (<tr key={l.id}><td>{l.id}</td><td>{l.name}</td><td>{l.email}</td>
      <td>{l.risk_score}</td></tr>
      ))}
      </tbody>
   </table>
</div>
)
}
