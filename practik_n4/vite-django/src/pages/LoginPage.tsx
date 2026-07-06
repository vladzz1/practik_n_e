import { useState } from "react"
import { useNavigate } from "react-router"
import { Link } from "react-router"
import * as z from "zod"
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import { FormInput } from "../components/FormInput/FormInput.tsx"
import { useLoginUserMutation } from "../services/usersApi.ts"
import { PasswordFormInput } from "../components/FormInput/PasswordFormInput.tsx"

const LoginPage = () => {
    const [loading, ] = useState(false)
    const [login] = useLoginUserMutation()
    const navigate = useNavigate()

    const formSchema = z.object({
        username: z.email({ message: "Введіть коректну електронну пошту" }),
        password: z.string().min(6, { message: "Пароль повинен містити щонайменше 6 символів" }).max(100, { message: "Пароль занадто довгий" })
    })

    const form = useForm<z.infer<typeof formSchema>>({
       resolver: zodResolver(formSchema),
       defaultValues: {
           username: "",
           password: ""
       }
    })

    const onSubmit = async (data: z.infer<typeof formSchema>) => {
        try {
            const response = await login(data).unwrap()
            console.log(response)
            navigate('/')
        }
        catch (error) {
            console.error(error)
        }
    }

    return (
        <div className="min-h-screen bg-slate-50 dark:bg-slate-950
        flex justify-center px-4 transition-colors duration-300">

            {/* Ambient glow */}
            <div className="pointer-events-none fixed inset-0 overflow-hidden">
                <div className="absolute -top-40 -left-40 w-[600px] h-[600px] rounded-full
                    bg-indigo-400/10 dark:bg-indigo-600/10 blur-3xl"
                />
                <div className="absolute -bottom-40 -right-40 w-[500px] h-[500px] rounded-full
                    bg-violet-400/10 dark:bg-violet-600/10 blur-3xl"
                />
            </div>

            {/* Card */}
            <div className="relative w-full max-w-[400px]">

                 {/*Logo mark */}
                <div className="flex justify-center mb-8">
                    <Link to="/" className="flex items-center gap-2.5 group select-none">
                        <div className="w-10 h-10 rounded-2xl
                            bg-gradient-to-br from-indigo-500 to-violet-600
                            flex items-center justify-center
                            shadow-lg shadow-indigo-500/30
                            group-hover:scale-105 transition-transform duration-200"
                        >
                            <span className="text-white font-bold text-base">К</span>
                        </div>
                        <span className="font-semibold text-slate-800 dark:text-slate-100 text-lg tracking-tight">
                            КозакиApp
                        </span>
                    </Link>
                </div>

                {/* Form card */}
                <div className="bg-white dark:bg-slate-900
                    border border-slate-200 dark:border-slate-800
                    rounded-2xl shadow-xl shadow-slate-200/50 dark:shadow-slate-900/50
                    p-8
                    transition-colors duration-300"
                >
                    <div className="mb-7">
                        <h1 className="text-2xl font-bold text-slate-900 dark:text-slate-50 tracking-tight mb-1">
                            Вхід до акаунту
                        </h1>
                        <p className="text-sm text-slate-500 dark:text-slate-400">
                            Вітаємо назад, козаче 👋
                        </p>
                    </div>

                    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">

                        <FormInput
                            control={form.control}
                            name="username"
                            label="Електронна пошта"
                            placeholder="kozak@sich.ua"
                        />

                        {/* Password */}
                        <PasswordFormInput
                            control={form.control}
                            name="password"
                            label="Пароль"
                        />
                        {/* Remember me */}
                        <div className="flex items-center gap-2.5 pt-1">
                            <input
                                id="remember"
                                type="checkbox"
                                className="w-4 h-4 rounded-md border-slate-300 dark:border-slate-600
                                    accent-indigo-500
                                    cursor-pointer"
                            />
                            <label htmlFor="remember" className="text-sm text-slate-600 dark:text-slate-400 cursor-pointer select-none">
                                Запам'ятати мене
                            </label>
                        </div>

                        {/* Submit */}
                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full mt-2 py-2.5 px-4 rounded-xl text-sm font-semibold
                                bg-gradient-to-r from-indigo-500 to-violet-600
                                text-white
                                shadow-md shadow-indigo-500/30
                                hover:shadow-lg hover:shadow-indigo-500/40
                                hover:scale-[1.01]
                                disabled:opacity-70 disabled:cursor-not-allowed disabled:scale-100
                                transition-all duration-200
                                flex items-center justify-center gap-2"
                        >
                            {loading ? (
                                <>
                                    <svg className="animate-spin w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"/>
                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
                                    </svg>
                                    Вхід…
                                </>
                            ) : "Увійти"}
                        </button>
                    </form>

                    {/* Divider */}
                    <div className="flex items-center gap-3 my-6">
                        <div className="flex-1 h-px bg-slate-200 dark:bg-slate-800" />
                        <span className="text-xs text-slate-400 dark:text-slate-600">або</span>
                        <div className="flex-1 h-px bg-slate-200 dark:bg-slate-800" />
                    </div>

                    {/* Google OAuth stub */}
                    <button
                        type="button"
                        className="w-full py-2.5 px-4 rounded-xl text-sm font-medium
                            bg-slate-50 dark:bg-slate-800
                            border border-slate-200 dark:border-slate-700
                            text-slate-700 dark:text-slate-300
                            hover:bg-slate-100 dark:hover:bg-slate-700/70
                            transition-all duration-200
                            flex items-center justify-center gap-2.5"
                    >
                        <svg width="16" height="16" viewBox="0 0 24 24">
                            <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                            <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                            <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"/>
                            <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                        </svg>
                        Увійти через Google
                    </button>
                </div>

                {/* Register link */}
                <p className="text-center text-sm text-slate-500 dark:text-slate-400 mt-6">
                    Ще немає акаунту?{" "}
                    <Link to="/registration" className="text-indigo-500 dark:text-indigo-400 font-medium hover:underline">
                        Зареєструватись
                    </Link>
                </p>
            </div>
        </div>
    )
}

export default LoginPage