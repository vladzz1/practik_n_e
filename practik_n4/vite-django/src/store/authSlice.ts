// src/store/authSlice.ts
import { createSlice, type PayloadAction } from '@reduxjs/toolkit'

interface AuthState {
    accessToken: string | null
    refreshToken: string | null
    username: string | null
    image: string | null
}

const initialState: AuthState = {
    accessToken: localStorage.getItem('accessToken'),
    refreshToken: localStorage.getItem('refreshToken'),
    username: localStorage.getItem('username'),
    image: localStorage.getItem('image')
}

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        setCredentials: (
            state,
            action: PayloadAction<{ access: string; refresh: string; username: string; image: string }>
        ) => {
            const { access, refresh, username, image } = action.payload
            state.accessToken = access
            state.refreshToken = refresh
            state.username = username
            state.image = image

            localStorage.setItem('accessToken', access)
            localStorage.setItem('refreshToken', refresh)
            localStorage.setItem('username', username)
            localStorage.setItem('image', image)
        },
        logout: (state) => {
            state.accessToken = null
            state.refreshToken = null
            state.username = null
            state.image = null

            localStorage.removeItem('accessToken')
            localStorage.removeItem('refreshToken')
            localStorage.removeItem('username')
            localStorage.removeItem('image')
        }
    }
})

export const { setCredentials, logout } = authSlice.actions
export default authSlice.reducer