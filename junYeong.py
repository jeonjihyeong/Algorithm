{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "준영\n"
     ]
    }
   ],
   "source": [
    "def validationKorean(txt):\n",
    "    isKorean = False\n",
    "    res = ''\n",
    "    for char in list(txt):\n",
    "        if ord('가') <= ord(char) <= ord('힣'):\n",
    "            if not isKorean:\n",
    "                isKorean = True\n",
    "                res += char\n",
    "            else:\n",
    "                res += char\n",
    "        else:\n",
    "            if isKorean:\n",
    "                break\n",
    "    return res\n",
    "\n",
    "txt = input('문자열을 입력하세요: ')\n",
    "res = validationKorean(txt)\n",
    "print(res)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
