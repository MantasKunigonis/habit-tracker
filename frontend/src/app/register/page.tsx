'use client'

import { useState } from "react"
import { useRouter } from "next/navigation"

export default function Register() {
  const router = useRouter()
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: ""
  })
  const [error, setError] = useState('')
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    })
  }
   const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')

    const res = await fetch('http://localhost:5000/register', {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams(form)
    })

    if (res.ok) {
      router.push('/login')
    } else {
      setError('Registration failed')
    }
  }

  return (
    <div className="row justify-content-center">
      <div className="col-md-6">
        <h2>Register</h2>

        {error && <div className="alert alert-danger">{error}</div>}

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Username</label>
            <input
              className="form-control"
              name="username"
              value={form.username}
              onChange={handleChange}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="email"
              className="form-control"
              name="email"
              value={form.email}
              onChange={handleChange}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              name="password"
              value={form.password}
              onChange={handleChange}
              required
            />
          </div>

          <button className="btn btn-primary w-100">
            Create Account
          </button>
        </form>
      </div>
    </div>
  )
}