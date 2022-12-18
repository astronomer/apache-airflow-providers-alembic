# Alembic

## Publish to Pypi
- [ ] update the version in `astronomer/providers/alembic/package.py` and in `setup.cfg`
- [ ] run `python setup.py sdist` to build
- [ ] run the following to upload, using a [pypi token](https://pypi.org/help/#apitoken) with access
```shell
twine upload -u __token__ -p pypi-Ag....................6Q dist/hw_team_party_parrot-0.1.0.tar.gz 
```
