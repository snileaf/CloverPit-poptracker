-- Synchronize separate visual toggle items with the progressive drawer item
local function drawerSync(code, value)
	local prog = Tracker:FindObjectForCode("progressivedrawer")
	if not prog then return end

	-- find the visual toggle items we added
	local vis = {
		Tracker:FindObjectForCode("progressivedrawer_stage1_item"),
		Tracker:FindObjectForCode("progressivedrawer_stage2_item"),
		Tracker:FindObjectForCode("progressivedrawer_stage3_item"),
		Tracker:FindObjectForCode("progressivedrawer_stage4_item"),
	}

	-- if any missing, abort
	for i=1,4 do
		if not vis[i] then return end
	end

	local active = prog.Active
	local stage = tonumber(prog.CurrentStage) or 0

	if not active or stage <= 0 then
		for i=1,4 do vis[i].Active = false end
		return
	end

	if stage > 4 then stage = 4 end
	for i=1,4 do
		vis[i].Active = (i <= stage)
	end
end

ScriptHost:AddWatchForCode("prog drawer sync", "progressivedrawer", drawerSync)
