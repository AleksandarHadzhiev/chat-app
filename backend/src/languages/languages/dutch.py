from src.languages.languages.base import Language 

class Dutch(Language):
    def __init__(self):
        self.data = """
            <svg viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="iconify iconify--twemoji w-2/3 h-2/3" preserveAspectRatio="xMidYMid meet" fill="#000000">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                    <path fill="#EEE" d="M0 14h36v8H0z"></path>
                    <path fill="#AE1F28" d="M32 5H4a4 4 0 0 0-4 4v5h36V9a4 4 0 0 0-4-4z"></path>
                    <path fill="#20478B" d="M4 31h28a4 4 0 0 0 4-4v-5H0v5a4 4 0 0 0 4 4z"></path>
                </g>
            </svg>
            <p style="padding-right:2px;">NL</p>
        """


    def get_data(self):
        return self.data