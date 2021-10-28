# ResponseSlimmer
you can use this executor to define which fields you want to drop from the flow's final response.

## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://ResponseSlimmer')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://ResponseSlimmer')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
