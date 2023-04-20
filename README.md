## 快速开始

支持 roberta 类型的模型。

### 安装依赖
```shell
pip install -r requirements.txt
```

### 训练 MLM 模型
默认使用 wikitext 数据集训练 roberta-base 模型，训练样本数为1000。
运行以下命令即可启动训练：
```shell
sh train-mlm.sh
```
可以修改 `train-mlm.sh` 来配置不同的训练参数。训练完毕后模型将保存在 `./model` 文件夹下。

### 训练 QA 模型
默认使用 squad 数据集对 `./model` 下的 roberta-base 模型进行微调，来实现 QA 的功能，训练样本数为1000。
运行以下命令即可启动训练：
```shell
sh train-qa.sh
```
可以修改 `train-qa.sh` 来配置不同的训练参数。训练完毕后模型将保存在 `./squad_model` 文件夹下。


### 构建 torchserve 文件
使用以下命令来构建 torchserve mar 文件，默认使用`./squad_model` 文件夹下的模型：
```shell
sh build-torch-serve-mar.sh
```
构建完成后 mar 文件将保存在 `model_store` 文件夹下。

### 启动 torchserve
使用以下命令启动 torchserve：
```shell
sh run-torchserve.sh
```

### 使用控制台进行交互
torchserve 启动成功后，使用以下命令启动控制台客户端：
```shell
python -u src/ts_scripts/console_client.py
```
或者使用实现 [torchserve grpc 接口](https://github.com/pytorch/serve/tree/master/frontend/server/src/main/resources/proto) 的外部 grpc 服务：
```shell
python -u src/ts_scripts/console_client.py --grpc-server <host>:<port>
```
即可进行交互。
示例：
```
Question:  who am i?
Answer:  user
Question:  who are you?
Answer:  robot
```

## 使用 Docker 进行部署

### 构建 Docker 镜像

CPU 版：
```shell
docker build . -t lm-demo -f .\Dockerfile-cpu
```

GPU 版：
```shell
docker build . -t lm-demo -f .\Dockerfile-gpu
```

### 启动镜像

运行以下命令并等待 torchserve 启动完成即可使用。
`MODEL_STORE_DIR`: torchserve 生成的 mar 文件所在的本地文件夹地址。
```shell
docker run -v ${MODEL_STORE_DIR}:/opt/model_store -it lm-demo
```
如果使用实现 [torchserve grpc 接口](https://github.com/pytorch/serve/tree/master/frontend/server/src/main/resources/proto) 的外部 grpc 服务：

```shell
docker run -it --entrypoint bin/bash lm-demo -c "python -u src/ts_scripts/console_client.py --grpc-server <host>:<port>"
```

## 使用 kubernetes 进行部署

覆盖 `lm-demo.yaml` 中 `namespace`，`image` 等字段。
注意：需要预先将模型存放至 `/opt/model_store` 目录下，可以在`lm-demo.yaml`中使用 `initContainers` 运行命令以获取模型。
然后执行命令：

```shell
kubectl apply -f lm-demo.yaml
```
