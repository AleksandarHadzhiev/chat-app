'use client'

import React from 'react';
import { ChatPage } from '@/components/Chat/ChatPage';
import { useRouter } from 'next/navigation';
export default function Home() {
  const router = useRouter()
  if (window.localStorage && window.localStorage.getItem("user") == null) {
    router.push("/login")
  }
  return (
    <ChatPage />
  );
}

