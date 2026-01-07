'use client'

import { useState, useEffect } from 'react';

export function useAuth() {
  const [user, setUser] = useState<{ username: string } | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function fetchUser() {
      try {
        const res = await fetch('/api/auth/me', {
          credentials: 'include', // send cookies
        })
        if (res.ok) {
          const data = await res.json()
          setUser(data)
        } else {
          setUser(null)
        }
      } catch (err) {
        console.error('Failed to fetch user:', err)
        setUser(null)
      } finally {
        setLoading(false)
      }
    }
    fetchUser()
  }, [setUser, setLoading])

  return { user, loading }
}