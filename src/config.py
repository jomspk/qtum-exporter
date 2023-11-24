#!/usr/bin/env python3

import typing
import os


class Config(object):
    
    QTUM_RPC_HOST: str = os.environ.get("QTUM_RPC_HOST", default="127.0.0.1")
    QTUM_RPC_PORT: int = int(os.environ.get("QTUM_RPC_PORT", default="13889"))  # Qtum testnet default port
    QTUM_RPC_USER: str = os.environ.get("QTUM_RPC_USER", default="test")
    QTUM_RPC_PASSWORD: str = os.environ.get("QTUM_RPC_PASSWORD", default="test1234")

    HASH_PS_BLOCKS: typing.List[int] = [
        int(block) for block in os.environ.get("HASH_PS_BLOCKS", default="-1,1,120").split(",") if block != str()
    ]
    SMART_FEE_BLOCKS: typing.List[int] = [
        int(block) for block in os.environ.get("SMART_FEE_BLOCKS", default="2,3,5,20").split(",") if block != str()
    ]

    METRICS_ADDRESS: str = os.environ.get("METRICS_ADDRESS", default="0.0.0.0")
    METRICS_PORT: int = int(os.environ.get("METRICS_PORT", default="6363"))

    TIMEOUT: float = float(os.environ.get("TIMEOUT", default=15))
    REFRESH_SECONDS: int = int(os.environ.get("REFRESH_SECONDS", default=5))
    LOGGING_LEVEL: str = os.environ.get("LOGGING_LEVEL", default="INFO")
