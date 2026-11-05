"""opencode-max: let opencode-go / opencode-zen accept ``max``.

Install: ``hermes plugins install <owner>/hermes-plugin-opencode-max --enable``

Why: Hermes core ships no reasoning vocabulary for these providers, so the
transport clamps unknown levels (``max`` -> ``xhigh``). This plugin subclasses
the *live* bundled profiles at import time, so upstream changes to those
profiles are inherited — only the one missing method is added. If upstream
ever declares its own vocabulary, this defers to it.
"""

from __future__ import annotations

try:
    from agent.reasoning_effort import OPENAI_COMPAT_WIRE_EFFORTS
    from providers import register_provider
    import providers as _providers_mod

    _orig_go = _providers_mod._REGISTRY.get("opencode-go")
    _orig_zen = _providers_mod._REGISTRY.get("opencode-zen")

    if _orig_go is not None:

        class _GoMax(type(_orig_go)):
            def supported_reasoning_efforts(self, model=None):
                try:
                    sup = super().supported_reasoning_efforts(model)
                except Exception:
                    sup = None
                return sup if sup is not None else OPENAI_COMPAT_WIRE_EFFORTS

        import copy as _copy

        _new_go = _copy.copy(_orig_go)
        _new_go.__class__ = _GoMax
        register_provider(_new_go)

    if _orig_zen is not None:

        class _ZenMax(type(_orig_zen)):
            def supported_reasoning_efforts(self, model=None):
                try:
                    sup = super().supported_reasoning_efforts(model)
                except Exception:
                    sup = None
                return sup if sup is not None else OPENAI_COMPAT_WIRE_EFFORTS

        import copy as _copy_zen

        _new_zen = _copy_zen.copy(_orig_zen)
        _new_zen.__class__ = _ZenMax
        register_provider(_new_zen)

except Exception:
    # Never break startup: without the override the route falls back to the
    # bundled behaviour (max -> xhigh).
    pass
