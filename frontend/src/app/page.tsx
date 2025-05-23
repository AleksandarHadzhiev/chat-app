'use client'

import React from 'react';
import { Chat } from '@/components/Chat/ChatPage';
import { useRouter } from 'next/navigation';
export default function Home() {
  const router = useRouter()
  if (localStorage && localStorage.getItem("user") == null) {
    router.push("/login")
  }
  return (
    <Chat />
  );
}

