'use client'


import React, { useContext, useEffect, useState } from 'react';
import TranslationLoader from '@/tools/TranslationLoader';
export default function Home() {
  // const myuuid = uuidv4();
  // const socket = new WebSocket("ws:/127.0.0.1:8000/ws/" + myuuid)

  // socket.addEventListener('open', (event) => {
  //   console.log("Connected to server");
  // })

  // socket.addEventListener('close', (event) => {
  //   console.log("Connected to server");
  // })

  // socket.onmessage = (event) => {
  //   console.log(event.data)
  // }
  // const { language } = useContext(ChildContext)
  // useEffect(() => {
  //   async function load() {
  //     const data = await new translationLoader().translationLoader(language, "login.json")
  //     console.log(data)
  //   }
  //   load()
  // }, [language])

  useEffect(() => {
    async function load() {
      const loader = new TranslationLoader("EN", "login")
      const response = await loader.getTranslatiosn()
      JSON.parse(response.data)
      console.log(JSON.parse(response.data).translations)
    }

    load()
  }, [])

  return (
    <h3>Welcome to the app</h3>
  );
}
