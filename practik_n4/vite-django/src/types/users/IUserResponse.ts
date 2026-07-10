export interface IUserResponse {
    message: string
    username: string
    image: string
    tokens: {
        refresh: string
        access: string
    }
}