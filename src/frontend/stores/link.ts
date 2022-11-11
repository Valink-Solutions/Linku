import { defineStore } from 'pinia'

export const useLinkStore = defineStore('links', {
    state: () => {
      return {
        // for initially empty lists
        userList: [] as UserInfo[],
        // for data that is not yet loaded
        user: null as UserInfo | null,
      }
    },
  })
  
  interface UserInfo {
    name: string
    age: number
  }