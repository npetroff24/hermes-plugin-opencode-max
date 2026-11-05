# opencode-max

Пусть `opencode-go` / `opencode-zen` принимают `max` вместо clamp в `xhigh`.

## Установка

```bash
hermes plugins install <owner>/hermes-plugin-opencode-max --enable
```

Перезапусти гейтвей/бекенд, чтобы подхватил:

- десктоп: перезапусти бэкенд
- сервер: `sudo systemctl restart hermes-gateway.service`

## Проверка

```bash
hermes chat -q "ответь одним словом: да" --reasoning max -Q --format text
```

В логах OpenCode свежая запись: `effort·max`.

## Как это работает

В ядре Hermes у этих провайдеров нет словаря reasoning — транспорт режет
неизвестное (`max` → `xhigh`). Плагин добавляет ровно один недостающий метод,
наследуя всё остальное от живых классов ядра, поэтому переживает `hermes update`.
Если ядро само починит словарь — плагин уступит.
