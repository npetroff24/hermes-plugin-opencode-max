# opencode-max — плагин max reasoning для OpenCode в Hermes Agent

**EN below.**

## Что это (коротко)

Плагин для [Hermes Agent](https://github.com/NousResearch/hermes-agent), который чинит одну бесящую вещь: ставишь reasoning `max` для моделей OpenCode (`opencode-go`, `opencode-zen` — например, `muse-spark`), а на сервер уходит `xhigh`.

С плагином:

```
ставишь max -> уходит max
```

Без плагина:

```
ставишь max -> уходит xhigh
```

## Почему так происходит

У провайдеров OpenCode в ядре Hermes нет словаря reasoning-уровней. Когда транспорт не знает уровень, он молча заменяет его ближайшим известным — `xhigh`. Ошибки нет, в настройках `max`, а в логах OpenCode `effort·xhigh`. Плагин добавляет ровно один недостающий метод — словарь уровней. Всё остальное (лимиты токенов, параметры моделей) по-прежнему берётся из ядра.

## Установка

```bash
hermes plugins install npetroff24/hermes-plugin-opencode-max --enable
```

Перезапусти бэкенд (десктоп) или гейтвей (сервер):

```bash
sudo systemctl restart hermes-gateway.service
```

## Проверка

```bash
hermes chat -q "ответь одним словом: да" --reasoning max -Q --format text
```

Свежая запись в логах OpenCode должна показать `effort·max`.

## Совместимость

- Hermes Agent с провайдерами `opencode-go` / `opencode-zen`
- Проверено с `muse-spark-1.3-contributor`
- Переживает `hermes update` — лежит отдельно от кода ядра
- Если ядро само починит словарь — плагин уступит и мешать не будет

## FAQ

**Это форк встроенного плагина?**
Нет. Плагин не копирует код ядра, а наследуется от живых классов при загрузке и добавляет один метод.

**Сломает ли обновления Hermes?**
Нет, он для этого и сделан: обновления ядра его не трогают.

**Зачем `max`, если есть `xhigh`?**
На сложных задачах (длинный код, архитектура, глубокий анализ) `max` даёт заметно более долгое и глубокое рассуждение. Разница видна в качестве ответа.

---

## EN

### What is this

A plugin for [Hermes Agent](https://github.com/NousResearch/hermes-agent) that fixes one annoying thing: you set reasoning effort `max` for OpenCode models (`opencode-go`, `opencode-zen` — e.g. `muse-spark`), but `xhigh` goes over the wire.

With the plugin:

```
you set max -> wire gets max
```

Without it:

```
you set max -> wire gets xhigh
```

### Why it happens

Hermes core ships no reasoning-effort vocabulary for the OpenCode providers. When the transport doesn't recognise a level, it silently clamps it to the nearest known one — `xhigh`. No error, settings say `max`, OpenCode logs say `effort·xhigh`. The plugin adds exactly the one missing method — the effort vocabulary. Everything else (token limits, per-model params) is still inherited from core.

### Install

```bash
hermes plugins install npetroff24/hermes-plugin-opencode-max --enable
```

Restart the backend (desktop) or gateway (server):

```bash
sudo systemctl restart hermes-gateway.service
```

### Verify

```bash
hermes chat -q "answer in one word: yes" --reasoning max -Q --format text
```

The fresh entry in OpenCode logs should show `effort·max`.

### Compatibility

- Hermes Agent with `opencode-go` / `opencode-zen` providers
- Verified with `muse-spark-1.3-contributor`
- Survives `hermes update` — lives outside core code
- If core ever ships the vocabulary itself, the plugin defers to it

### FAQ

**Is this a fork of a bundled plugin?**
No. It doesn't copy core code — it subclasses the live core classes at load time and adds one method.

**Will it break Hermes updates?**
No, that's the point: core updates never touch it.

**Why `max` when `xhigh` exists?**
On hard tasks (big code, architecture, deep analysis) `max` reasons noticeably longer and deeper. The difference shows in answer quality.
