{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNUCESOkyJnW6kZ7Gy8fJj9",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shivangi-js/python-30-day-challenge/blob/main/Day1loops.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gUe6oglL1QSc",
        "outputId": "dfa650c9-cc84-4b89-d9d3-6f6d927825f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the number : 50\n",
            "21\n",
            "42\n"
          ]
        }
      ],
      "source": [
        "num = int(input(\"enter the number : \"))\n",
        "i = 1\n",
        "\n",
        "while i <= num:\n",
        "  if i%3==0 and i%7==0:\n",
        "    print(i)\n",
        "  i+=1\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,51):\n",
        "  if i%3==0 and i%5==0:\n",
        "    print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eCb6OkSU3tvt",
        "outputId": "ce8f9b67-77d3-4588-9cb4-2f027f51673e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "30\n",
            "45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"enter your number : \"))\n",
        "\n",
        "i = 1\n",
        "total = 0\n",
        "while i<=num:\n",
        "  total = total + i\n",
        "  i+=1\n",
        "print(total\n",
        "      )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UXyTQrxw4Fei",
        "outputId": "3d916a54-042b-477d-ee68-fd642f75ddd7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your number : 50\n",
            "1275\n"
          ]
        }
      ]
    }
  ]
}