def purge_expired(self):
    """
    Purge souveraine :
    - retire les IDs dont l'âge dépasse max_age
    - maintient la cohérence entre queue, index et timestamps
    - garantit un état interne propre et déterministe
    """
    now = int(time.time())
    expired = []

    # 1. Identification des IDs expirés
    for m_id, ts in self.timestamps.items():
        if now - ts > self.max_age:
            expired.append(m_id)

    if not expired:
        return  # Rien à faire, état déjà propre

    # 2. Suppression cohérente
    for m_id in expired:
        self.timestamps.pop(m_id, None)
        self.index.discard(m_id)

    # 3. Reconstruction propre de la deque
    # (on ne retire pas du milieu : on reconstruit)
    self.queue = deque(
        [m_id for m_id in self.queue if m_id in self.index],
        maxlen=self.max_cache_size
    )

    # 4. Log souverain
    logger.debug(
        f"[Sentinel] Purge souveraine : {len(expired)} IDs retirés "
        f"(cache={len(self.queue)}, index={len(self.index)})"
    )
